"""
Validateurs avancés pour le module automobile (données, sécurité, RGPD, multitenancy).
"""
def validate_vin(vin):
    """Valide le format du VIN (Vehicle Identification Number)."""
    return len(vin) == 17 and vin.isalnum()

def validate_annee(annee):
    """Valide l’année du véhicule (>=1886)."""
    return isinstance(annee, int) and annee >= 1886

def validate_proprietaire(proprietaire_id, tenant_id):
    """Valide que le propriétaire appartient bien au tenant (multitenancy)."""
    # À implémenter avec la logique d’accès multitenant
    return True
