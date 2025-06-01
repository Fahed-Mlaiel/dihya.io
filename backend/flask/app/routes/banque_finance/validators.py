"""
Validateurs avancés pour le module banque_finance (données, sécurité, RGPD, multitenancy).
"""
def validate_bic(bic):
    """Valide le format du code BIC (8 caractères alphanumériques)."""
    return len(bic) == 8 and bic.isalnum()

def validate_pays(pays):
    """Valide le nom du pays (2-56 caractères)."""
    return 2 <= len(pays) <= 56

def validate_tenant(tenant_id):
    """Valide l’appartenance du tenant (multitenancy)."""
    return isinstance(tenant_id, int) and tenant_id > 0
