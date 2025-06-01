import pytest
from .example_plugin import ExampleLogistiquePlugin

def test_example_plugin_process():
    plugin = ExampleLogistiquePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
