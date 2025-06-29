#!/usr/bin/env python3
"""
Script Lead Dev : Remplissage automatique des fichiers du dossier analytics avec du code métier généré par OpenAI
- Lit la clé API depuis .env (OPENAI_API_KEY)
- Parcourt tous les fichiers du dossier analytics (récursif)
- Génère un prompt métier pour chaque fichier (nom, extension, contexte, cahier des charges)
- Envoie la requête à l’API OpenAI (GPT-4o)
- Écrit le code généré dans chaque fichier (si vide ou à enrichir)
- Log chaque étape, évite les doublons, économise le quota
- Ne met ni placeholder, ni TODO, ni commentaire inutile

Usage :
    python3 enrich_analytics_with_openai.py
"""
import os
import openai
from dotenv import load_dotenv

ANALYTICS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analytics")
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "enrich_analytics.log")
CAHIER_DES_CHARGES = """
Génération automatique de modules analytics (backend, frontend, plugins, docs, i18n, etc.)
- Respecte la logique de chaque fichier selon son nom, son extension, sa place dans l’architecture
- Code métier réel, production ready, sans placeholder, sans TODO, sans commentaire inutile
- Technologies : Python, JS, React, Node.js, etc.
- Respecte les standards d’industrialisation, sécurité, RGPD, DevOps, documentation, i18n, accessibilité
- Structure modulaire, extensible, clé en main
"""

# Chargement de la clé API
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

MODEL = "gpt-4-1106-preview"
MAX_TOKENS = 2048
TEMPERATURE = 0.2


def is_text_file(filename):
    return any(filename.endswith(ext) for ext in [".py", ".js", ".jsx", ".json", ".md", ".yaml", ".yml", ".sh", ".tf"])

def get_prompt(filepath, relpath):
    return f"""Tu es un Lead Dev Full-Stack & Architecte Solution. Génère le contenu complet, métier, production ready, pour le fichier suivant :
- Chemin : {relpath}
- Extension : {os.path.splitext(filepath)[1]}
- Cahier des charges : {CAHIER_DES_CHARGES}
- Ne mets ni placeholder, ni TODO, ni commentaire inutile. Code direct, prêt à l’emploi.
"""

def extract_code_only(text):
    import re
    # Cherche le premier bloc de code markdown
    matches = re.findall(r"```[a-zA-Z0-9]*\n([\s\S]*?)```", text)
    if matches:
        return matches[0].strip()
    # Sinon, retourne tout le texte (fallback)
    return text.strip()

def enrich_file(filepath, relpath, log, stop_counter):
    if not is_text_file(filepath):
        log.append(f"[IGNORÉ] {relpath} (non textuel)")
        return stop_counter
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if content:
        log.append(f"[SKIP] {relpath} (déjà rempli)")
        return stop_counter
    prompt = get_prompt(filepath, relpath)
    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": "Tu es un Lead Dev Full-Stack & Architecte Solution."},
                      {"role": "user", "content": prompt}],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )
        code = extract_code_only(response.choices[0].message.content)
        # Contrôle conformité : pas de texte explicatif, pas de placeholder, pas de TODO, pas de commentaire
        if (not code or
            any(x in code.lower() for x in ["placeholder", "todo", "exemple", "explanat", "note:", "ce fichier", "ceci est", "this file"]) or
            code.startswith("Le fichier") or code.startswith("// Le fichier") or code.startswith("# Le fichier") or code.startswith("/* Le fichier")):
            log.append(f"[NON CONFORME] {relpath} (contrôle Lead Dev)")
            stop_counter += 1
            if stop_counter >= 5:
                log.append("[STOP] 5 fichiers non conformes détectés. Arrêt pour correction.")
                raise Exception("Arrêt automatique : 5 fichiers non conformes.")
            return stop_counter
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        log.append(f"[OK] {relpath} (rempli)")
    except Exception as e:
        log.append(f"[ERREUR] {relpath} : {e}")
    return stop_counter

def main():
    log = []
    stop_counter = 0
    for root, dirs, files in os.walk(ANALYTICS_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            relpath = os.path.relpath(filepath, ANALYTICS_DIR)
            stop_counter = enrich_file(filepath, relpath, log, stop_counter)
            if stop_counter >= 5:
                break
        if stop_counter >= 5:
            break
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        for line in log:
            f.write(line + "\n")
    print(f"Remplissage terminé. Voir le log : {LOG_FILE}")

if __name__ == "__main__":
    main()
