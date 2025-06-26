import os
import mimetypes
import struct
import sys
# import xml.etree.ElementTree as ET
import google.generativeai as genai
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

def generate(text_content: str, api_key: str, output_path: str, speaker1_voice: str = "Zephyr", speaker2_voice: str = "Puck", speaking_rate: Optional[str] = None, pitch: Optional[str] = None):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-preview-tts",
        generation_config={
            "response_mime_type": 'audio/wav',
            "speech_config": {
                "output_audio_encoding": "LINEAR16_UNCOMPRESSED",
                "sample_rate_hertz": 24000,
                "speaking_rate": 1.0,
                "pitch": 0.0,
                "volume_gain_db": 0.0
            }
        }
    )

    # スタイル調整のためのプロンプトを追加
    modified_text_content = text_content
    if speaking_rate == "slow":
        modified_text_content = "ゆっくり話してください.\n" + modified_text_content
    elif speaking_rate == "fast":
        modified_text_content = "速く話してください.\n" + modified_text_content

    if pitch == "high":
        modified_text_content = "高いピッチで話してください.\n" + modified_text_content
    elif pitch == "low":
        modified_text_content = "低いピッチで話してください.\n" + modified_text_content
 
    contents = [
        modified_text_content
    ]

    response = model.generate_content(
        contents=contents
    )
    
    file_index = 0
    audio_data = b''
    for chunk in response:
        if (
            chunk.candidates is None
            or chunk.candidates[0].content is None
            or chunk.candidates[0].content.parts is None
        ):
            continue
        if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
            file_name = f"{output_path}_{file_index}.wav"
            file_index += 1
            inline_data = chunk.candidates[0].content.parts[0].inline_data
            data_buffer = inline_data.data
            
            file_extension = get_file_extension_from_mime_type(inline_data.mime_type)
            if file_extension is None:
                file_extension = mimetypes.guess_extension(inline_data.mime_type)
                if file_extension is None:
                    print(f"Warning: Could not determine file extension for MIME type: {inline_data.mime_type}. Defaulting to .mp3")
                    file_extension = ".mp3"
            save_binary_file(file_name, data_buffer, inline_data.mime_type)
        else:
            print(chunk.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python test_tts.py <テキストファイルパス> [speaker1_voice] [speaker2_voice] [speaking_rate] [pitch]")
        sys.exit(1)
    
    text_file_path = sys.argv[1]
    
    speaker1_voice = sys.argv[2] if len(sys.argv) > 2 else "Zephyr"
    speaker2_voice = sys.argv[3] if len(sys.argv) > 3 else "Puck"
    speaking_rate = sys.argv[4] if len(sys.argv) > 4 else None
    pitch = sys.argv[5] if len(sys.argv) > 5 else None

    output_base_name = os.path.splitext(text_file_path)[0]
    output_file_path = f"{output_base_name}_output"

    try:
        with open(text_file_path, "r", encoding="utf-8") as f:
            script_content = f.read()
        generate(script_content, os.environ.get("GEMINI_API_KEY"), output_file_path, speaker1_voice, speaker2_voice, speaking_rate, pitch)
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません - {text_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"エラーが発生しました: {e}") 