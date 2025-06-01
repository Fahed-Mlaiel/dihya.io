import pytest
from .example_plugin import ExampleTourismePlugin

def test_example_plugin_process():
    plugin = ExampleTourismePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
