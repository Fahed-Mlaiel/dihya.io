"""
Validateurs avancés pour le module btp (données, sécurité, RGPD, multitenancy).
"""
def validate_nom(nom):
    return 1 <= len(nom) <= 100

def validate_secteur(secteur):
    return 1 <= len(secteur) <= 50

def validate_tenant(tenant_id):
    return isinstance(tenant_id, int) and tenant_id > 0
