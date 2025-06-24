import os
import mimetypes
import struct
import sys
import xml.etree.ElementTree as ET
from google.genai import Client
from google.genai.types import (Content, Part, GenerateContentConfig, SpeechConfig, MultiSpeakerVoiceConfig, SpeakerVoiceConfig, VoiceConfig, PrebuiltVoiceConfig)
from dotenv import load_dotenv
from typing import Optional

# 既知のMIMEタイプと拡張子のマッピング
def get_file_extension_from_mime_type(mime_type):
    # セミコロン以降のパラメータを削除して、純粋なMIMEタイプ部分を取得
    clean_mime_type = mime_type.split(';')[0].strip()
    mime_type_map = {
        "audio/mpeg": ".mp3",
        "audio/wav": ".wav",
        "audio/L16": ".wav", # LPCMオーディオのマッピングを追加
        # 必要に応じて他のオーディオMIMEタイプを追加
    }
    return mime_type_map.get(clean_mime_type, None)

# .envファイルをロード
load_dotenv()

def save_binary_file(file_name, data, mime_type):
    # WAVヘッダーを追加する関数
    def add_wav_header(pcm_data, num_channels=1, sample_rate=24000, sample_width_bytes=2):
        data_size = len(pcm_data)
        file_size = 36 + data_size
        byte_rate = num_channels * sample_rate * sample_width_bytes
        block_align = num_channels * sample_width_bytes

        header = b'RIFF'
        header += struct.pack('<I', file_size)
        header += b'WAVE'
        header += b'fmt '
        header += struct.pack('<I', 16)  # Subchunk1Size for PCM
        header += struct.pack('<H', 1)   # AudioFormat (PCM = 1)
        header += struct.pack('<H', num_channels)
        header += struct.pack('<I', sample_rate)
        header += struct.pack('<I', byte_rate)
        header += struct.pack('<H', block_align)
        header += struct.pack('<H', sample_width_bytes * 8) # BitsPerSample
        header += b'data'
        header += struct.pack('<I', data_size)
        return header + pcm_data

    # inline_data.mime_typeがaudio/L16の場合にWAVヘッダーを追加
    if mime_type.startswith("audio/L16"): # mime_typeで判定
        data_to_save = add_wav_header(data)
    else:
        data_to_save = data

    with open(file_name, "wb") as f:
        f.write(data_to_save)
    print(f"File saved to: {file_name}")

def generate(ssml_content: str, speaker1_voice: str = "Zephyr", speaker2_voice: str = "Puck"):
    client = Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-preview-tts"

    # SSMLを解析し、プロンプトテキストを構築
    # 名前空間を明示的に定義
    SSML_NAMESPACE = "{http://www.w3.org/2001/10/synthesis}"
    ET.register_namespace('', 'http://www.w3.org/2001/10/synthesis') # デフォルト名前空間を登録
    
    root = ET.fromstring(ssml_content)
    prompt_text = ""

    for p_tag in root.findall(f'.//{SSML_NAMESPACE}p'):
        for s_tag in p_tag.findall(f'.//{SSML_NAMESPACE}s'):
            speaker_name = s_tag.get('speaker', 'Speaker 1') # デフォルトはSpeaker 1
            
            segment_instructions = []

            # s_tag内のすべてのテキストコンテンツを抽出
            # element.itertext()を使用して、要素とその子孫要素のテキストコンテンツを順に取得
            full_s_tag_text = "".join(s_tag.itertext()).strip()
            
            # prosodyタグの処理を分離して、指示を先頭に追加
            for element in s_tag.findall(f'.//{SSML_NAMESPACE}prosody'):
                rate = element.get('rate')
                if rate == "80%":
                    segment_instructions.append("(ゆっくりと話してください)")
                elif rate == "120%":
                    segment_instructions.append("(速く話してください)")
                elif rate == "normal":
                    segment_instructions.append("(通常の速度で話してください)")

            # breakタグの処理
            for element in s_tag.findall(f'.//{SSML_NAMESPACE}break'):
                time = element.get('time')
                if time:
                    segment_instructions.append(f"(約{time}のポーズ)")

            # プロンプトテキストの構築
            if segment_instructions:
                speaker_dialogue = " ".join(segment_instructions) + " " + full_s_tag_text
            else:
                speaker_dialogue = full_s_tag_text

            if speaker_dialogue.strip(): # 空でないか確認
                prompt_text += f"{speaker_name}: {speaker_dialogue.strip()}\n"

    print(f"Generated Prompt Text:\n---\n{prompt_text}---\n") # Debug print

    contents = [
        Content(
            role="user",
            parts=[
                Part.from_text(text=prompt_text),
            ],
        ),
    ]
    generate_content_config = GenerateContentConfig(
        temperature=1,
        response_modalities=[
            "audio",
        ],
        speech_config=SpeechConfig(
            multi_speaker_voice_config=MultiSpeakerVoiceConfig(
                speaker_voice_configs=[
                    SpeakerVoiceConfig(
                        speaker="Speaker 1",
                        voice_config=VoiceConfig(
                            prebuilt_voice_config=PrebuiltVoiceConfig(
                                voice_name=speaker1_voice
                            )
                        ),
                    ),
                    SpeakerVoiceConfig(
                        speaker="Speaker 2",
                        voice_config=VoiceConfig(
                            prebuilt_voice_config=PrebuiltVoiceConfig(
                                voice_name=speaker2_voice
                            )
                        ),
                    ),
                ]
            ),
        ),
    )

    file_index = 0
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.candidates is None or not chunk.candidates:
            print("No candidates in chunk.")
            continue

        candidate = chunk.candidates[0]
        if candidate.content is None or not candidate.content.parts:
            print("No content parts in candidate.")
            continue

        first_part = candidate.content.parts[0]
        if first_part.inline_data and first_part.inline_data.data:
            file_name = f"output_audio_{file_index}"
            file_index += 1
            inline_data = first_part.inline_data
            data_buffer = inline_data.data
            
            file_extension = get_file_extension_from_mime_type(inline_data.mime_type)
            
            if file_extension is None:
                file_extension = mimetypes.guess_extension(inline_data.mime_type)
                if file_extension is None:
                    print(f"Warning: Could not determine file extension for MIME type: {inline_data.mime_type}. Defaulting to .mp3")
                    file_extension = ".mp3"
            save_binary_file(f"{file_name}{file_extension}", data_buffer, inline_data.mime_type)
        else:
            # テキストチャンクが返された場合、その内容を出力
            if chunk.text:
                print(f"Received non-audio chunk (text): {chunk.text}")
            else:
                print("Received non-audio chunk (no text content).")

# convert_to_wav関数とparse_audio_mime_type関数は、
# mimetypes.guess_extensionがNoneを返す問題の回避策として不要になったため削除します。

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python test_tts.py <SSMLファイルパス> [speaker1_voice] [speaker2_voice]")
        sys.exit(1)
    
    ssml_file_path = sys.argv[1]
    
    speaker1_voice = sys.argv[2] if len(sys.argv) > 2 else "Zephyr"
    speaker2_voice = sys.argv[3] if len(sys.argv) > 3 else "Puck"

    try:
        with open(ssml_file_path, "r", encoding="utf-8") as f:
            ssml_content = f.read()
        generate(ssml_content, speaker1_voice, speaker2_voice)
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません - {ssml_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        sys.exit(1) 