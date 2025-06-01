import pytest
from .example_plugin import ExampleEducationPlugin

def test_example_plugin_process():
    plugin = ExampleEducationPlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
