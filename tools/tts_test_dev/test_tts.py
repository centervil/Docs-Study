import os
import mimetypes
import struct
from google.genai import Client
from google.genai.types import (Content, Part, GenerateContentConfig, SpeechConfig, MultiSpeakerVoiceConfig, SpeakerVoiceConfig, VoiceConfig, PrebuiltVoiceConfig)
from dotenv import load_dotenv

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

def save_binary_file(file_name, data):
    f = open(file_name, "wb")
    f.write(data)
    f.close()
    print(f"File saved to: {file_name}")

def generate():
    client = Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-preview-tts"
    contents = [
        Content(
            role="user",
            parts=[
                Part.from_text(text="""これはGemini TTS APIのテストです。正しく音声が生成されるか確認します。
Speaker 1: ユーザーが求めているのは、音声合成の精度向上と、より自然な発話です。
Speaker 2: そのためには、多様な音声データを用いた学習と、文脈に応じた感情表現の調整が不可欠です。"""),
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
                                voice_name="Zephyr"
                            )
                        ),
                    ),
                    SpeakerVoiceConfig(
                        speaker="Speaker 2",
                        voice_config=VoiceConfig(
                            prebuilt_voice_config=PrebuiltVoiceConfig(
                                voice_name="Puck"
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
        if (
            chunk.candidates is None
            or chunk.candidates[0].content is None
            or chunk.candidates[0].content.parts is None
        ):
            continue
        if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
            file_name = f"output_audio_{file_index}"
            file_index += 1
            inline_data = chunk.candidates[0].content.parts[0].inline_data
            data_buffer = inline_data.data
            
            # まずカスタムマッピングを試す
            file_extension = get_file_extension_from_mime_type(inline_data.mime_type)
            
            if file_extension is None:
                # カスタムマッピングで見つからなければ、mimetypesモジュールも試す
                file_extension = mimetypes.guess_extension(inline_data.mime_type)
                if file_extension is None:
                    # どちらでも見つからなければ、デフォルトを.mp3に設定し警告
                    print(f"Warning: Could not determine file extension for MIME type: {inline_data.mime_type}. Defaulting to .mp3")
                    file_extension = ".mp3"
            save_binary_file(f"{file_name}{file_extension}", data_buffer)
        else:
            print(chunk.text)

# convert_to_wav関数とparse_audio_mime_type関数は、
# mimetypes.guess_extensionがNoneを返す問題の回避策として不要になったため削除します。

if __name__ == "__main__":
    generate() 