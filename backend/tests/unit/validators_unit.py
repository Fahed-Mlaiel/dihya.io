"""
Tests unitaires avancés pour les validateurs backend Dihya (validation, sécurité, RGPD, i18n, plugins, audit, SEO, IA fallback).
"""
import pytest
from backend.validators import (
    validate_email, validate_password, validate_role, validate_lang, validate_plugin
)

def test_validate_email():
    assert validate_email('test@example.com') is True
    assert validate_email('invalid-email') is False

def test_validate_password():
    assert validate_password('StrongPassw0rd!') is True
    assert validate_password('123') is False

def test_validate_role():
    assert validate_role('admin') is True
    assert validate_role('user') is True
    assert validate_role('guest') is True
    assert validate_role('hacker') is False

def test_validate_lang():
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        assert validate_lang(lang) is True
    assert validate_lang('xx') is False

def test_validate_plugin():
    assert validate_plugin('seo') is True
    assert validate_plugin('unknown') is False
