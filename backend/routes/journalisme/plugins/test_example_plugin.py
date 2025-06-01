import pytest
from .example_plugin import ExampleJournalismePlugin

def test_example_plugin_process():
    plugin = ExampleJournalismePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
