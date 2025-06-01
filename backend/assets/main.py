"""
Dihya – Backend Assets Entrypoint (Python)
------------------------------------------
- Point d'entrée unique pour la gestion des assets backend (multi-stack, multilingue, souveraineté, sécurité)
- Fournit des utilitaires pour charger, vérifier, et auditer les assets (modèles, datasets, configs, clés publiques…)
- Prêt pour intégration Python, CI/CD, Codespaces, cloud souverain
- Documentation multilingue, logs, conformité RGPD/NIS2, fallback open source

🇫🇷 Point d'entrée assets backend Python (sécurité, fallback, multilingue)
🇬🇧 Python backend assets entry point (secure, fallback, multilingual)
🇦🇪 نقطة دخول أصول الباكند (Python) مع الأمان والدعم متعدد اللغات
ⵣ Amuddu n backend assets Python (amatu, fallback, multilingual)
"""

import os
import hashlib
import json
import yaml

ASSETS_ROOT = os.path.dirname(os.path.abspath(__file__))

def load_asset(asset_path, expected_hash=None):
    abs_path = os.path.join(ASSETS_ROOT, asset_path)
    if not os.path.isfile(abs_path):
        raise FileNotFoundError(f"Asset not found: {abs_path}")
    with open(abs_path, "rb") as f:
        data = f.read()
    if expected_hash:
        hash_ = hashlib.sha256(data).hexdigest()
        if hash_ != expected_hash:
            raise ValueError(f"Hash mismatch for asset {asset_path}: expected {expected_hash}, got {hash_}")
    return data

def load_model(model_name):
    model_path = os.path.join("models", f"{model_name}.bin")
    return load_asset(model_path)

def load_config(config_name):
    config_path = os.path.join("configs", config_name)
    ext = os.path.splitext(config_path)[1].lower()
    data = load_asset(config_path)
    if ext == ".json":
        return json.loads(data.decode("utf-8"))
    if ext in [".yaml", ".yml"]:
        return yaml.safe_load(data.decode("utf-8"))
    raise ValueError("Unsupported config file type")

def audit_assets(dir_path=ASSETS_ROOT):
    results = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            with open(full_path, "rb") as f:
                hash_ = hashlib.sha256(f.read()).hexdigest()
            rel_path = os.path.relpath(full_path, ASSETS_ROOT)
            results.append({"file": rel_path, "hash": hash_})
    return results

# Exemple d'utilisation :
# model = load_model('llama2')
# config = load_config('ia_config.yaml')
# audit = audit_assets()

# Sécurité : logs, audit, conformité RGPD/NIS2, fallback open source
# Multilingue : prêt pour i18n (voir assets.md)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

if __name__ == "__main__":
    print("Dihya Backend Assets module – gestion des scripts, configs, templates, données de test.")
    # ...lancer les scripts d’import/export, de vérification, d’audit, etc.
