# helpers/helpers.py – Helpers métiers ultra avancés (Python)
def get_model_by_id(fixtures, id):
    """Retourne le modèle 3D par ID."""
    return next((f for f in fixtures if f.get('id') == id), None)

def anonymize_fixture(fixture):
    """Anonymise un fixture pour la conformité RGPD."""
    anonymized = fixture.copy()
    anonymized['name'] = 'anonymized'
    anonymized['owner'] = None
    return anonymized

def audit_fixture(fixture):
    """Audit de conformité et d’accessibilité sur un fixture."""
    return {
        'has_name': bool(fixture.get('name')),
        'has_vertices': bool(fixture.get('vertices')),
        'is_accessible': 'description' in fixture,
    }
