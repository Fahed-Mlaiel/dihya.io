"""
fixtures_validator.py - Validation avancée des fixtures Threed (Python)
"""
def is_valid_3d_model(model):
    return bool(model and isinstance(model.get('id'), str) and isinstance(model.get('vertices'), list) and isinstance(model.get('faces'), int))

def is_valid_user(user):
    return bool(user and isinstance(user.get('id'), str) and isinstance(user.get('role'), str))
