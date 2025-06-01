import pytest
from .example_plugin import ExampleSciencePlugin

def test_example_plugin_process():
    plugin = ExampleSciencePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
