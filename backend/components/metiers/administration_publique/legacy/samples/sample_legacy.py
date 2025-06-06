"""
Exemple ultra avancé de script legacy pour compatibilité Threed (3D)
Inclut : modèle multi-format, edge cases, audit, traçabilité.
"""

def sample_legacy_model():
    return {
        'legacy_id': 'sample-legacy-001',
        'legacy_name': 'AncienCube',
        'points': [ [0,0,0], [1,0,0], [1,1,0], [0,1,0] ],
        'surfaces': [ [0,1,2,3] ],
        'created_at': '2001-01-01T00:00:00Z',
        'meta': { 'source': 'legacy', 'migrated': False },
        'auditTrail': [
            { 'date': '2025-06-03T12:00:00Z', 'action': 'created' },
            { 'date': '2025-06-03T12:05:00Z', 'action': 'checked' }
        ]
    }

def sample_legacy_edge_case():
    return {
        'legacy_name': 'SansID',
        'points': [],
        'version': 2,
        'meta': { 'source': 'legacy', 'migrated': False }
    }
