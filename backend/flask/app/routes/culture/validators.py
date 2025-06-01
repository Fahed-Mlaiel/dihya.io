"""
Validateurs avancés pour le module culture (données, sécurité, RGPD, multitenancy).
"""
def validate_nom(nom):
    return 1 <= len(nom) <= 100

def validate_type(type_):
    return 1 <= len(type_) <= 50

def validate_tenant(tenant_id):
    return isinstance(tenant_id, int) and tenant_id > 0
