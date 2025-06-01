"""
Gestion dynamique des plugins backend Dihya : chargement, sandbox, audit, multilingue, RGPD, extensibilité, CI/CD-ready
"""
import os
import importlib

def load_plugins(app):
    plugins_dir = os.path.join(os.path.dirname(__file__), '../plugins')
    if not os.path.isdir(plugins_dir):
        app.logger.warning(f"Dossier plugins introuvable : {plugins_dir}")
        return
    for fname in os.listdir(plugins_dir):
        if fname.endswith('.py') and not fname.startswith('__'):
            mod_name = f"Dihya.backend.plugins.{fname[:-3]}"
            try:
                mod = importlib.import_module(mod_name)
                if hasattr(mod, 'register_plugin'):
                    mod.register_plugin(app)
                app.logger.info(f"Plugin chargé : {mod_name}")
            except Exception as e:
                app.logger.error(f"Erreur chargement plugin {mod_name} : {e}")
