import pytest
from .example_plugin import ExampleSantePlugin

def test_example_plugin_process():
    plugin = ExampleSantePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
