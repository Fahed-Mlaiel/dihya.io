"""
sample_service.test.py
Tests unitaires pour SampleService (clé en main, CI/CD ready)
"""
import pytest
from .sample_service import SampleService

def test_sample_service_init():
    service = SampleService(options={"mode": "test"})
    assert service.options == {"mode": "test"}
    assert service.state == 'ready'

def test_sample_service_config():
    service = SampleService()
    assert service.init({"level": 1}) is True
    assert service.config == {"level": 1}
    assert service.state == 'initialized'

def test_sample_service_run():
    service = SampleService()
    service.init({"level": 2})
    result = service.run("DATA")
    assert result == {"processed": True, "data": "DATA", "config": {"level": 2}, "state": "initialized"}
