import os
import json
from pathlib import Path

def get_visible_dirs_and_files(path: Path):
    folders = []
    files = []

    for item in path.iterdir():
        if item.name.startswith('.') or item.name == 'index.json':
            continue
        if item.is_dir():
            folders.append(item.name)
        elif item.is_file():
            files.append(item.name)

    return sorted(folders), sorted(files)

def generate_index(root_path: str):
    root = Path(root_path)

    for path in root.rglob('*'):
        if path.is_dir():
            folders, files = get_visible_dirs_and_files(path)
            index = {
                "folders": folders,
                "files": files
            }
            index_path = path / 'index.json'
            with open(index_path, 'w') as f:
                json.dump(index, f, indent=2)

    # Создаём index.json в корне отдельно (если его нет)
    folders, files = get_visible_dirs_and_files(root)
    index = {
        "folders": folders,
        "files": files
    }
    index_path = root / 'index.json'
    with open(index_path, 'w') as f:
        json.dump(index, f, indent=2)

if __name__ == '__main__':
    generate_index('resources')
