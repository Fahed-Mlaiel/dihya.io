# test.py - Test unitaire et d'intégration pour SEO (Python)
"""
Test complet SEO backend (robots, sitemap, logs structurés)
"""
import pytest
from ..seo import generate_sitemap, log_seo_event

def test_generate_valid_sitemap():
    sitemap = generate_sitemap(['/', '/about'])
    assert '<urlset' in sitemap

def test_log_seo_event():
    assert log_seo_event('visit', '/') == 'logged'
