import pytest
from .example_plugin import ExampleManufacturingPlugin

def test_example_plugin_process():
    plugin = ExampleManufacturingPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
