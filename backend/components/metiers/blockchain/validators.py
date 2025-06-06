"""
Validators Blockchain – Dihya Coding
Sécurité, RGPD, audit, plugins, multilingue, tests, monitoring.
"""

# Validators Blockchain

def validate_blockchain(data):
    if not isinstance(data, dict):
        raise ValueError('Data must be a dict')
    if 'name' not in data or not data['name']:
        raise ValueError('Le nom du projet blockchain est requis')
    return True
