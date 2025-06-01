import pytest
from .example_plugin import ExampleArtsPlugin

def test_example_plugin_process():
    plugin = ExampleArtsPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
