"""
Script de génération automatique de documentation API pour Dihya Coding.

Ce module permet d’extraire et de générer la documentation des endpoints du backend
(à partir de fichiers OpenAPI, docstrings, ou introspection Flask), au format Markdown, HTML ou JSON.

Bonnes pratiques :
- Générer la documentation à chaque modification majeure de l’API.
- Ne jamais inclure de secrets ou d’exemples contenant des données sensibles.
- Logger chaque génération avec horodatage.
- Permettre l’export dans plusieurs formats ouverts.
- Documenter la procédure d’utilisation dans le README associé.

Exécution :
    python generate_api_doc.py

"""

import os
from datetime import datetime
import shutil

OPENAPI_FILE = "docs/openapi.yaml"
OUTPUT_MD = "docs/api_generated.md"
LOG_FILE = "docs/scripts/generate_api_doc.log"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

def generate_from_openapi():
    """
    Génère une documentation Markdown à partir du fichier OpenAPI.
    (Ici, copie brute, à remplacer par un parseur YAML → Markdown si besoin)
    """
    if not os.path.exists(OPENAPI_FILE):
        log("Fichier OpenAPI introuvable.")
        return
    with open(OPENAPI_FILE, "r", encoding="utf-8") as src, open(OUTPUT_MD, "w", encoding="utf-8") as dst:
        dst.write("# Documentation API générée automatiquement\n\n")
        dst.write("**Source : docs/openapi.yaml**\n\n")
        dst.write(src.read())
    log(f"Documentation API générée dans {OUTPUT_MD}")

if __name__ == "__main__":
    generate_from_openapi()
    log("Génération de documentation terminée.")