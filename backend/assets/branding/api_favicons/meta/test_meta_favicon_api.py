import pytest
from .meta_favicon_api import meta_favicon_api

"""
Tests avancés sur les métadonnées du favicon API Dihya : RGPD, accessibilité, multilingue, plugins, audit, SEO, CI/CD.
"""

def test_meta_favicon_api_structure():
    assert isinstance(meta_favicon_api, dict)
    assert "description" in meta_favicon_api
    assert "fr" in meta_favicon_api["description"]
    assert "en" in meta_favicon_api["description"]
    assert meta_favicon_api["accessibility"]["contrast"] == "AAA"
    assert meta_favicon_api["rgpd"]["conformite"] is True
    assert meta_favicon_api["audit"]["result"] == "passed"
    assert "favicon-generator" in meta_favicon_api["plugins"]
    assert meta_favicon_api["integration"]["django"] is True
    assert meta_favicon_api["integration"]["rest"] is True
    assert meta_favicon_api["integration"]["graphql"] is True
    assert "robots" in meta_favicon_api["seo"]
    assert "sitemap" in meta_favicon_api["seo"]

def test_meta_favicon_api_multilingue():
    langs = ["fr", "en", "ar", "tzm", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"]
    for lang in langs:
        assert lang in meta_favicon_api["description"]
        assert lang in meta_favicon_api["accessibility"]["alt_text"]

def test_meta_favicon_api_rgpd_audit():
    assert meta_favicon_api["rgpd"]["conformite"] is True
    assert meta_favicon_api["rgpd"]["anonymisation"] is True
    assert meta_favicon_api["rgpd"]["exportable"] is True
    assert meta_favicon_api["audit"]["result"] == "passed"
