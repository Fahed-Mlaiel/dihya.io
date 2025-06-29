import os

def is_empty_or_quasi_empty(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [l for l in f if l.strip()]
            if len(lines) == 0:
                return True
            if len(lines) <= 10:
                # Considéré quasi-vide si <= 10 lignes non vides
                return True
        return False
    except Exception:
        # Fichiers binaires ou non lisibles
        return True

def main():
    root = '/workspaces/dihya.io/blueprints'
    count = 0
    empty_files = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if is_empty_or_quasi_empty(filepath):
                count += 1
                empty_files.append(filepath)
    print(f"Fichiers vides/quasi-vides restants: {count}")
    for f in empty_files:
        print(f)

if __name__ == "__main__":
    main()
