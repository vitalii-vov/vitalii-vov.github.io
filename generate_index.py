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

def generate_all_folders_from_files(root_path: Path) -> set[Path]:
    all_dirs = set()

    # Идём по всем файлам, даже глубоко
    for file in root_path.rglob('*'):
        if file.is_file():
            for parent in file.parents:
                if root_path in parent.parents or parent == root_path:
                    all_dirs.add(parent)
    return all_dirs

def generate_index(root_path: str):
    root = Path(root_path).resolve()
    if not root.exists():
        print(f"Path {root} doesn't exist")
        return

    all_dirs = generate_all_folders_from_files(root)

    for path in all_dirs:
        folders, files = get_visible_dirs_and_files(path)
        index = {
            "folders": folders,
            "files": files
        }
        index_path = path / 'index.json'
        index_path.write_text(json.dumps(index, indent=2))

if __name__ == '__main__':
    generate_index('resources')
