# mock_helper.py – Mock ultra avancé helpers (clé en main)
def mock_validation_data():
    """
    Mock de validation pour tests RGPD, audit, accessibilité
    :return: dict
    """
    from datetime import datetime
    return {
        'id': 1,
        'user': 'mocked',
        'email': 'mock@example.com',
        'consent': True,
        'timestamp': datetime.utcnow().isoformat()
    }
