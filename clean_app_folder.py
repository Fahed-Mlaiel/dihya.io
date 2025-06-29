#!/usr/bin/env python3
"""
Script Lead Dev : Nettoyage des fichiers parasites et doublons dans /app
- Supprime tous les fichiers dont le nom contient un commentaire (#) ou une description (ex : ' # ...')
- Supprime les fichiers qui sont des doublons évidents (même nom avant le #)
- Ne touche pas aux vrais fichiers métiers

Usage :
    python3 clean_app_folder.py
"""
import os
import re

APP_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")

REMOVED = []

pattern = re.compile(r"(.+?)\s+#.*")

for root, dirs, files in os.walk(APP_ROOT):
    for file in files:
        if '#' in file or 'Checklist' in file or 'professionnelle' in file or 'détaillée' in file or file.strip().startswith('---'):
            try:
                os.remove(os.path.join(root, file))
                REMOVED.append(os.path.join(root, file))
            except Exception:
                pass
        else:
            # Supprime les doublons (ex : 'file.js' et 'file.js  # ...')
            match = pattern.match(file)
            if match:
                base = match.group(1).strip()
                base_path = os.path.join(root, base)
                if os.path.exists(base_path):
                    try:
                        os.remove(os.path.join(root, file))
                        REMOVED.append(os.path.join(root, file))
                    except Exception:
                        pass

print("--- FICHIERS SUPPRIMÉS ---")
for r in REMOVED:
    print(r)
print("Nettoyage terminé.")
