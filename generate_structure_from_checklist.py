#!/usr/bin/env python3
"""
Script de génération automatique de la structure du projet à partir de CHECKLIST_STRUCTURE_DIHYAIO_SCRIPT_READY.txt
- Crée tous les dossiers et fichiers listés (sauf ceux liés aux tests)
- Ignore les doublons et les chemins invalides
- Ne touche pas aux fichiers/dossiers déjà existants

Usage :
    python3 generate_structure_from_checklist.py

Lead Dev: Génération clé en main, industrialisation.
"""
import os

CHECKLIST_FILE = "CHECKLIST_STRUCTURE_DIHYAIO_SCRIPT_READY.txt"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

IGNORED_KEYWORDS = ["/tests/", "tests/", "/tests\\", "tests\\"]


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
                os.makedirs(dir_path, exist_ok=True)
            # Fichier
            else:
                file_path = os.path.join(PROJECT_ROOT, line)
                dir_path = os.path.dirname(file_path)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path, exist_ok=True)
                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f_out:
                        pass  # Fichier vide

if __name__ == "__main__":
    main()
    print("Structure générée avec succès (hors tests).")
