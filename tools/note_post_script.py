from oasis import OASIS
import os
import sys
from pathlib import Path

def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else 'tools/sample-article'
    folder_path = Path(folder)
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"[ERROR] 指定ディレクトリが存在しません: {folder_path}")
        sys.exit(1)

    # OASISインスタンス生成（AIモデル指定なし）
    oasis = OASIS()
    # Note.com投稿のみ有効
    result = oasis.process_folder(
        str(folder_path),
        post_to_qiita=False,
        post_to_note=True,
        post_to_wp=False,
        post_to_zenn=False
    )
    print(result)

if __name__ == '__main__':
    main() 