#!/usr/bin/env python3
"""
Script Lead Dev : Génération robuste de la structure du dossier app selon la checklist nettoyée
- Crée tous les dossiers et fichiers listés dans CHECKLIST_STRUCTURE_APP_CLEAN.txt
- Ignore les doublons et les chemins invalides
- Ne touche pas aux fichiers/dossiers déjà existants
- Ne crée pas de fichiers de tests

Usage :
    python3 generate_app_structure_from_checklist.py
"""
import os

CHECKLIST_FILE = os.path.join("app", "CHECKLIST_STRUCTURE_APP_CLEAN.txt")
APP_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")
IGNORED_KEYWORDS = ["/tests/", "tests/", "/tests\\", "tests\\"]

CREATED = []
SKIPPED = []

def is_ignored(line):
    return any(kw in line for kw in IGNORED_KEYWORDS)

def main():
    if not os.path.exists(APP_ROOT):
        os.makedirs(APP_ROOT, exist_ok=True)
    with open(CHECKLIST_FILE, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if is_ignored(line):
                continue
            abs_path = os.path.join(APP_ROOT, line)
            if line.endswith("/"):
                if not os.path.exists(abs_path):
                    os.makedirs(abs_path, exist_ok=True)
                    CREATED.append(f"Dossier créé : {abs_path}")
                else:
                    SKIPPED.append(f"Dossier déjà existant : {abs_path}")
            else:
                dir_path = os.path.dirname(abs_path)
                if dir_path and not os.path.exists(dir_path):
                    os.makedirs(dir_path, exist_ok=True)
                    CREATED.append(f"Dossier créé (pour fichier) : {dir_path}/")
                if not os.path.exists(abs_path):
                    with open(abs_path, "w", encoding="utf-8") as f_out:
                        pass
                    CREATED.append(f"Fichier créé : {abs_path}")
                else:
                    SKIPPED.append(f"Fichier déjà existant : {abs_path}")
    print("\n--- CONTRÔLE STRUCTURE APP ---")
    print(f"Créés : {len(CREATED)}")
    for c in CREATED:
        print(c)
    print(f"Déjà existants : {len(SKIPPED)}")
    for s in SKIPPED:
        print(s)
    print("\nStructure app générée et contrôlée avec succès (hors tests).")

if __name__ == "__main__":
    main()
