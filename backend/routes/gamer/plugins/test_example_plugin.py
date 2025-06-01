import pytest
from .example_plugin import ExampleGamerPlugin

def test_example_plugin_process():
    plugin = ExampleGamerPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
