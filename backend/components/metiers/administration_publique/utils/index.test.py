"""
index.test.py – Tests d'intégration Python pour tous les utilitaires Threed
"""
from . import utils

def test_utils_expose_audit():
    assert hasattr(utils, 'auditThreed')

def test_utils_expose_i18n():
    assert hasattr(utils, 'i18n')

def test_utils_expose_pluginManager():
    assert hasattr(utils, 'PluginManager') or hasattr(utils, 'pluginManager')

def test_utils_expose_log_info():
    assert hasattr(utils, 'log_info') or hasattr(utils, 'logger')

def test_utils_expose_record_metric():
    assert hasattr(utils, 'record_metric') or hasattr(utils, 'metrics')
