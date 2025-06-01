import pytest
from .example_plugin import ExampleVoicePlugin

def test_example_plugin_process():
    plugin = ExampleVoicePlugin()
    data = {'foo': 'bar'}
    result = plugin.process(data)
    assert result['example'] == 'ok'
