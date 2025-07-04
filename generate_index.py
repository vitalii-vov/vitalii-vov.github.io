import os
import json

def generate_index(root):
    for current_dir, dirs, files in os.walk(root):
        # Не исключаем dirs[:] — иначе os.walk() не зайдёт в подкаталоги
        visible_dirs = [d for d in dirs if not d.startswith('.')]
        visible_files = [f for f in files if not f.startswith('.') and f != 'index.json']

        index = {
            "folders": sorted(visible_dirs),
            "files": sorted(visible_files)
        }

        index_path = os.path.join(current_dir, 'index.json')
        with open(index_path, 'w') as f:
            json.dump(index, f, indent=2)

if __name__ == '__main__':
    generate_index('resources')
