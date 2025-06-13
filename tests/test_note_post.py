import subprocess
import sys
from pathlib import Path

def test_no_args():
    result = subprocess.run([sys.executable, 'tools/note_post.py'], capture_output=True, text=True)
    assert result.returncode != 0
    assert 'usage:' in result.stderr or 'usage:' in result.stdout

def test_invalid_folder():
    result = subprocess.run([
        sys.executable, 'tools/note_post.py', '--folder', 'not_exist_dir'
    ], capture_output=True, text=True)
    assert result.returncode != 0
    assert '存在しません' in result.stdout 