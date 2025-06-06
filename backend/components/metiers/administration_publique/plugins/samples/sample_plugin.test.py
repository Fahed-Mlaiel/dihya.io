"""
sample_plugin.test.py
Tests unitaires pour SamplePlugin (clé en main, CI/CD ready)
"""
import pytest
from .sample_plugin import SamplePlugin

def test_sample_plugin_init():
    plugin = SamplePlugin(options={"mode": "test"})
    assert plugin.options == {"mode": "test"}

def test_sample_plugin_config():
    plugin = SamplePlugin()
    assert plugin.init({"level": 1}) is True
    assert plugin.config == {"level": 1}

def test_sample_plugin_run():
    plugin = SamplePlugin()
    plugin.init({"level": 2})
    result = plugin.run("DATA")
    assert result == {"processed": True, "data": "DATA", "config": {"level": 2}}
