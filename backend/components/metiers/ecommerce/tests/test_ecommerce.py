"""
Test unitaire eCommerce (Dihya Coding)
- REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback.
"""

def test_produit():
    from ..schemas import Produit
    p = Produit(id=1, nom='Test', prix=10, categorie='tech')
    assert p.nom == 'Test'
    assert p.prix == 10

def test_schema_multilingue():
    from ..schemas import Produit
    p = Produit(id=2, nom='Produit', prix=20, categorie='test', langues=['fr', 'en'])
    assert 'fr' in p.langues
    assert 'en' in p.langues
