# tests/test_config.py — Tests automatisés de la configuration Flask Dihya
"""
Tests unitaires et de conformité pour le module de configuration backend Flask Dihya.
Couvre la sécurité, la robustesse, la conformité RGPD et la personnalisation multi-environnement.
"""
import sys
import os
import pytest

# Correction du chemin d'import pour compatibilité workspace, CI/CD, et respect de la logique Dihya
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import Config

def test_env_default():
    assert Config.ENV in ["development", "production", "test"]

def test_debug_flag():
    assert isinstance(Config.DEBUG, bool)

def test_secret_key():
    assert Config.SECRET_KEY != "change-me"
    assert len(Config.SECRET_KEY) >= 8

def test_allowed_hosts():
    assert isinstance(Config.ALLOWED_HOSTS, list)
    assert "localhost" in Config.ALLOWED_HOSTS

def test_cors_origins():
    assert isinstance(Config.CORS_ORIGINS, list)
    assert "*" in Config.CORS_ORIGINS or len(Config.CORS_ORIGINS) > 0

def test_log_level():
    assert Config.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def test_languages():
    assert "fr" in Config.LANGUAGES
    assert Config.DEFAULT_LANGUAGE in Config.LANGUAGES

def test_security_flags():
    assert Config.CSRF_ENABLED is True
    assert Config.XSS_PROTECTION is True
    assert Config.CONTENT_SECURITY_POLICY is True

def test_testing_flag():
    assert isinstance(Config.TESTING, bool)
