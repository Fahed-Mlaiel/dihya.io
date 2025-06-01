"""
Dihya – Module 3D Templates Initializer
---------------------------------------
Ce module permet l’import, l’extension et la gestion des templates 3D pour la plateforme Dihya (VR/AR, visualisation, simulation, assets, scènes, IA 3D).

🇫🇷 Initialisation du package 3D templates (sécurité, extensibilité, multilingue)
🇬🇧 3D templates package initialization (security, extensibility, multilingual)
🇦🇪 تهيئة حزمة قوالب ثلاثية الأبعاد (الأمان، التوسعة، متعدد اللغات)
ⵣ Tazwart n templates 3D (amatu, extensibility, multilingual)

Ce fichier rend le dossier importable comme package Python, prêt pour l’extension par plugins, assets, IA, ou scripts métiers.
"""

# Import de base pour l’auto-discovery des templates/plugins 3D
import os

def discover_3d_templates():
    """
    Découvre dynamiquement tous les templates 3D présents dans le dossier.
    Returns:
        list: Liste des chemins relatifs des templates 3D détectés.
    """
    templates_dir = os.path.dirname(__file__)
    templates = []
    for fname in os.listdir(templates_dir):
        if fname.endswith(('.obj', '.gltf', '.glb', '.fbx', '.dae', '.json', '.py')) and not fname.startswith('__'):
            templates.append(fname)
    return templates

# Expose la fonction de découverte pour les modules externes
__all__ = ['discover_3d_templates']

# Sécurité : aucun code exécutable à l’import, pas d’exécution dynamique non contrôlée
# Extensible : ajoutez vos templates, assets, scripts ou plugins 3D dans ce dossier
# Multilingue : voir doc/README pour la documentation multilingue
