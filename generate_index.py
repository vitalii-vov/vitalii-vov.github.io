import os
import json

def generate_index(root):
    for current_dir, dirs, files in os.walk(root):
        # Пропускаем скрытые папки
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.') and f != 'index.json']

        folders = sorted(dirs)
        file_names = sorted(files)

        index = {
            "folders": folders,
            "files": file_names
        }

        index_path = os.path.join(current_dir, 'index.json')
        with open(index_path, 'w') as f:
            json.dump(index, f, indent=2)

if __name__ == '__main__':
    generate_index('resources')
