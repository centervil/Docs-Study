import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="指定ディレクトリ内のMarkdownをNote.comに投稿する（OASIS利用）")
    parser.add_argument("--folder", required=True, help="投稿対象のMarkdownファイルが入ったディレクトリ")
    parser.add_argument("--note-email", required=False, help="Note.comのメールアドレス（省略時は.env参照）")
    parser.add_argument("--note-password", required=False, help="Note.comのパスワード（省略時は.env参照）")
    parser.add_argument("--note-user-id", required=False, help="Note.comのユーザーID（省略時は.env参照）")
    parser.add_argument("--firefox-headless", action="store_true", help="Firefoxをヘッドレスで実行")
    args = parser.parse_args()

    folder_path = Path(args.folder)
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"[ERROR] 指定ディレクトリが存在しません: {folder_path}")
        sys.exit(1)

    # OASISコマンド組み立て
    cmd = [
        sys.executable.replace("python", "oasis"),
        "--folder_path", str(folder_path),
        "--note",
        "--llm-model", "None" # LLMを無効化
    ]
    if args.note_email:
        cmd += ["--note-email", args.note_email]
    if args.note_password:
        cmd += ["--note-password", args.note_password]
    if args.note_user_id:
        cmd += ["--note-user-id", args.note_user_id]
    if args.firefox_headless:
        cmd += ["--firefox-headless"]

    print("[INFO] 実行コマンド: " + " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        print(f"[ERROR] 投稿処理に失敗しました (exit code: {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)

if __name__ == "__main__":
    main()

