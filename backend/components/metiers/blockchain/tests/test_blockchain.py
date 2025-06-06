"""
Test unitaire Blockchain – Dihya Coding
Sécurité, RGPD, audit, plugins, multilingue, tests, monitoring.

Exemple d’utilisation : pytest test_blockchain.py
"""
def test_blockchain_project_schema():
    from ..schemas import BlockchainProjectSchema
    data = {
        'id': '1',
        'name': 'Test',
        'owner': 'Testeur',
        'lang': 'fr',
        'plugins': ['audit'],
        'created_at': '2025-06-01T00:00:00Z'
    }
    schema = BlockchainProjectSchema(**data)
    assert schema.name == 'Test'
    assert 'audit' in schema.plugins

def test_blockchain_rgpd_export():
    from ..blockchain import BlockchainProject
    p = BlockchainProject('Test RGPD', 'User')
    export = p.export_rgpd()
    assert 'name' in export and export['name'] == 'Test RGPD'
    p.anonymize()
    assert p.owner is None
