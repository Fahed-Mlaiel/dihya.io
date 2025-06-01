import pytest
from .example_plugin import ExampleBlockchainPlugin

def test_example_plugin_process():
    plugin = ExampleBlockchainPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
