import os

try:
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'jack_secrets')

    with open(file_path, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print(f"Fehler: Datei '{file_path}' nicht gefunden.")
except Exception as e:
    print(f"Fehler beim Lesen der Datei '{file_path}': {e}")