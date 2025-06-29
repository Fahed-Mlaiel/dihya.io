#!/usr/bin/env python3
"""
Script de génération automatique de la structure racine à partir de CHECKLIST_RACINE_DIHYAIO_PRO.txt
- Crée tous les dossiers et fichiers listés (hors tests)
- Ignore les doublons et les chemins invalides
- Ne touche pas aux fichiers/dossiers déjà existants
- Contrôle et log des créations

Usage :
    python3 generate_root_structure_from_checklist.py

Lead Dev: Génération clé en main, contrôle inclus.
"""
import os

CHECKLIST_FILE = "CHECKLIST_RACINE_DIHYAIO_PRO.txt"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
IGNORED_KEYWORDS = ["/tests/", "tests/", "/tests\\", "tests\\"]

CREATED = []
SKIPPED = []


def is_ignored(line):
    return any(kw in line for kw in IGNORED_KEYWORDS)

def main():
    with open(os.path.join(PROJECT_ROOT, CHECKLIST_FILE), "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if is_ignored(line):
                continue
            # Dossier
            if line.endswith("/"):
                dir_path = os.path.join(PROJECT_ROOT, line)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path, exist_ok=True)
                    CREATED.append(f"Dossier créé : {line}")
                else:
                    SKIPPED.append(f"Dossier déjà existant : {line}")
            # Fichier
            else:
                file_path = os.path.join(PROJECT_ROOT, line)
                dir_path = os.path.dirname(file_path)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path, exist_ok=True)
                    CREATED.append(f"Dossier créé (pour fichier) : {dir_path}/")
                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f_out:
                        pass  # Fichier vide
                    CREATED.append(f"Fichier créé : {line}")
                else:
                    SKIPPED.append(f"Fichier déjà existant : {line}")
    # Contrôle final
    print("\n--- CONTRÔLE STRUCTURE RACINE ---")
    print(f"Créés : {len(CREATED)}")
    for c in CREATED:
        print(c)
    print(f"Déjà existants : {len(SKIPPED)}")
    for s in SKIPPED:
        print(s)
    print("\nStructure racine générée et contrôlée avec succès (hors tests).")

if __name__ == "__main__":
    main()
