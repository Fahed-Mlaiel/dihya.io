"""
guide_plugins.py - Guide d'intégration et d'utilisation des plugins Threed (Python)
"""

def add_plugin(manager, plugin):
    manager.register(plugin)

def activate_plugin(plugin):
    if hasattr(plugin, 'activate'):
        plugin.activate()

def deactivate_plugin(plugin):
    if hasattr(plugin, 'deactivate'):
        plugin.deactivate()

# Exemples avancés d'intégration de plugins :
#
# Ajout dynamique
# class MyPlugin:
#     def activate(self):
#         pass
#     def deactivate(self):
#         pass
# add_plugin(manager, MyPlugin())
#
# Sécurité : vérifier la signature du plugin
# def is_trusted(plugin):
#     return hasattr(plugin, 'activate')
#
# Audit : journaliser l'activation
# def audit_activation(plugin):
#     print(f"[AUDIT] Activation du plugin: {plugin}")
#
# CI/CD : tests automatisés sur les plugins (voir tests/plugins_test.py)
