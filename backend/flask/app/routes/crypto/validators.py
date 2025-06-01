"""
Validateurs avancés pour le module crypto (données, sécurité, RGPD, multitenancy).
"""
def validate_nom(nom):
    return 1 <= len(nom) <= 100

def validate_symbole(symbole):
    return 1 <= len(symbole) <= 10

def validate_tenant(tenant_id):
    return isinstance(tenant_id, int) and tenant_id > 0
