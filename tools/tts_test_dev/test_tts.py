import os
import struct
import sys
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional

# WAVファイルに関する定数
WAV_CONSTANTS = {
    "NUM_CHANNELS": 1,
    "SAMPLE_RATE": 24000,
    "SAMPLE_WIDTH_BYTES": 2,  # 2バイト = 16ビット
}

# .envファイルをロード
load_dotenv()

# WAVヘッダーを生成する関数
def create_wav_header(pcm_data_size: int, num_channels: int = WAV_CONSTANTS["NUM_CHANNELS"],
                      sample_rate: int = WAV_CONSTANTS["SAMPLE_RATE"],
                      sample_width_bytes: int = WAV_CONSTANTS["SAMPLE_WIDTH_BYTES"]) -> bytes:
    file_size = 36 + pcm_data_size
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
    header += struct.pack('<I', pcm_data_size)
    return header

def save_binary_file(file_name: str, data: bytes, mime_type: str):
    data_to_save = data
    if mime_type.startswith("audio/L16"):
        data_to_save = create_wav_header(len(data)) + data
    
    try:
        with open(file_name, "wb") as f:
            f.write(data_to_save)
        print(f"File saved to: {file_name}")
    except IOError as e:
        print(f"Error saving file {file_name}: {e}")

def generate(text_content: str, api_key: str, output_path: str, speaking_rate: Optional[float] = None, pitch: Optional[float] = None):
    genai.configure(api_key=api_key)

    speech_config = {
        "sample_rate_hertz": WAV_CONSTANTS["SAMPLE_RATE"],
        "speaking_rate": speaking_rate if speaking_rate is not None else 1.0,
        "pitch": pitch if pitch is not None else 0.0,
        "volume_gain_db": 0.0
    }
 
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-preview-tts",
        generation_config={
            "response_mime_type": 'audio/wav',
            "speech_config": speech_config
        }
    )

    response = model.generate_content(
        contents=[text_content]
    )
    
    audio_data_buffer = b''
    for chunk in response:
        if chunk.candidates and chunk.candidates[0].content and chunk.candidates[0].content.parts:
            part = chunk.candidates[0].content.parts[0]
            if part.inline_data and part.inline_data.data:
                audio_data_buffer += part.inline_data.data
            elif chunk.text:
                print(chunk.text)
        else:
            print("Warning: Received an empty or malformed chunk.")

    if audio_data_buffer:
        file_name = f"{output_path}.wav"
        save_binary_file(file_name, audio_data_buffer, "audio/L16")
    else:
        print("Warning: No audio data generated.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python test_tts.py <テキストファイルパス> [speaking_rate (float)] [pitch (float)]")
        sys.exit(1)
    
    text_file_path = sys.argv[1]
    
    speaking_rate_arg = None
    if len(sys.argv) > 2:
        try:
            speaking_rate_arg = float(sys.argv[2])
        except ValueError:
            print("エラー: speaking_rate は数値である必要があります。")
            sys.exit(1)

    pitch_arg = None
    if len(sys.argv) > 3:
        try:
            pitch_arg = float(sys.argv[3])
        except ValueError:
            print("エラー: pitch は数値である必要があります。")
            sys.exit(1)

    output_base_name = os.path.splitext(text_file_path)[0]
    output_file_path = f"{output_base_name}_output"

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("エラー: GEMINI_API_KEY 環境変数が設定されていません。")
        sys.exit(1)

    try:
        with open(text_file_path, "r", encoding="utf-8") as f:
            script_content = f.read()
        generate(script_content, api_key, output_file_path, speaking_rate=speaking_rate_arg, pitch=pitch_arg)
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません - {text_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"エラーが発生しました: {e}") 