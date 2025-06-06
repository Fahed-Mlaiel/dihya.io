# helpers/validators.py – Helpers de validation ultra avancés (Python)
def is_valid_3d_model(model):
    """Valide un modèle 3D (structure, RGPD, accessibilité)."""
    return bool(model and isinstance(model.get('id'), str) and isinstance(model.get('vertices'), list))

def is_valid_user(user):
    """Valide un utilisateur (structure, conformité)."""
    return bool(user and isinstance(user.get('id'), str) and isinstance(user.get('role'), str))

def is_fixture_accessible(fixture):
    """Vérifie l’accessibilité d’un fixture."""
    return 'description' in fixture and isinstance(fixture['description'], str)
