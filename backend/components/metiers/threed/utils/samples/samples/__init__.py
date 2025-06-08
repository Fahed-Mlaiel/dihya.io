# Initialisation avancée Python pour auto-discovery, import/export centralisé, structure modulaire, clé en main.

import os

def discover_samples(directory):
    samples = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and not file.startswith('__init__'):
                samples.append(os.path.join(root, file))
    return samples
