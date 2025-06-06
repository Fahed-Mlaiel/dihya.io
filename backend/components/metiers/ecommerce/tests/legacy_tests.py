"""
Tests legacy pour eCommerce (Dihya Coding)
- Compatibilité ascendante, audit, RGPD, plugins, souveraineté numérique.
"""

def test_legacy_api():
    from ..legacy.api_legacy import getLegacyProduct
    produit = getLegacyProduct(1)
    assert produit['legacy'] is True

def test_legacy_audit():
    from ..legacy.api_legacy import auditLegacy
    result = auditLegacy('test', 'user')
    assert result['status'] == 'legacy_audit'
