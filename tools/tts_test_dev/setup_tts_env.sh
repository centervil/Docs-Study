#!/bin/bash

# 既存の仮想環境を削除（もしあれば）
rm -rf venv_tts

# 新しい仮想環境を作成
/usr/bin/python3 -m venv venv_tts

# 仮想環境をアクティベート
source venv_tts/bin/activate

# 必要なモジュールをインストール
pip install google-genai python-dotenv

echo "TTS開発環境のセットアップが完了しました。" 