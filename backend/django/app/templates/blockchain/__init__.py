"""
Dihya – Initialisation du module Templates Blockchain
----------------------------------------------------
Ce package permet la gestion, l’import et l’extension des templates métiers pour la blockchain (contrats intelligents, transactions, audits, NFT, IA, plugins).

🇫🇷 Initialisation du package blockchain (sécurité, extensibilité, multilingue)
🇬🇧 Blockchain templates package initialization (security, extensibility, multilingual)
🇦🇪 تهيئة حزمة قوالب البلوكشين (الأمان، التوسعة، متعدد اللغات)
ⵣ Tazwart n templates n blockchain (amatu, extensibility, multilingual)

Ce fichier rend le dossier importable comme package Python, prêt pour l’extension par plugins, assets, IA, ou scripts métiers.
"""

import os

def discover_blockchain_templates():
    """
    Découvre dynamiquement tous les templates blockchain présents dans le dossier.
    Returns:
        list: Liste des chemins relatifs des templates détectés.
    """
    templates_dir = os.path.dirname(__file__)
    templates = []
    for fname in os.listdir(templates_dir):
        if fname.endswith(('.json', '.yaml', '.yml', '.py', '.md', '.sol', '.pdf')) and not fname.startswith('__'):
            templates.append(fname)
    return templates

__all__ = ['discover_blockchain_templates']

# Sécurité : aucun code exécutable à l’import, pas d’exécution dynamique non contrôlée
# Extensible : ajoutez vos templates, assets, scripts ou plugins métiers dans ce dossier
# Multilingue : voir doc/README pour la documentation multilingue
