# plugins_helper.test.py
# Tests unitaires Python pour plugins_helper
from .plugins_helper import is_valid_plugin_name

def test_is_valid_plugin_name():
    assert is_valid_plugin_name('plugin-1')
    assert is_valid_plugin_name('plugin_2')
    assert not is_valid_plugin_name('plugin!')
    assert not is_valid_plugin_name('')
