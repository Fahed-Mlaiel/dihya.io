# Initialisation avancée Python pour la découverte automatique des modules legacy JS
import os

def discover_legacy_js(directory):
    legacy = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                legacy.append(os.path.join(root, file))
    return legacy
