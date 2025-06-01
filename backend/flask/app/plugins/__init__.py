"""
Module d'initialisation pour la gestion des plugins/extensibilité dans Dihya Coding.

Ce package permet de charger dynamiquement des plugins Python pour étendre les fonctionnalités du backend Flask.
Chaque plugin doit respecter les conventions de sécurité, validation et documentation du projet.

Bonnes pratiques :
- Chaque plugin doit être documenté et validé avant activation.
- Les plugins ne doivent pas compromettre la sécurité ou la stabilité du backend.
- Prévoir un mécanisme d'activation/désactivation des plugins.
- Charger dynamiquement les plugins déclarés dans la configuration.

Exemple d'import :
    from backend.flask.app.plugins import load_plugins

"""

import importlib
import os

def load_plugins(plugin_folder="app/plugins"):
    """
    Charge dynamiquement tous les plugins Python présents dans le dossier plugins.
    Retourne une liste de modules plugins chargés.
    """
    plugins = []
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.plugins.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)
                plugins.append(module)
            except Exception as e:
                print(f"Erreur lors du chargement du plugin {module_name} : {e}")
    return plugins

def load_plugin(name):
    return {"name": name, "enabled": True}

def is_plugin_enabled(name):
    return True
