# pluginManager.sample.py
"""Exemple d'utilisation du pluginManager (Python)"""
from ..core.pluginManager import PluginManager

pm = PluginManager()
pm.register('test', lambda: 'ok')
print('Résultat plugin test:', pm.run('test'))
