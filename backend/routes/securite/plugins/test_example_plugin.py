import pytest
from .example_plugin import ExampleSecuritePlugin

def test_example_plugin_process():
    plugin = ExampleSecuritePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
