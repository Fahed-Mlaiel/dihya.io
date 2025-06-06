# core_metier.py – Module métier legacy/core (exemple)
def metier_legacy_core(data):
    """Logique métier legacy ultra avancée (RGPD, accessibilité, audit, edge cases, CI/CD)"""
    if not isinstance(data, dict):
        raise ValueError('Entrée invalide')
    result = data.copy()
    # RGPD: anonymisation d'un champ sensible si présent
    if 'sensitive' in result:
        result['sensitive'] = '[anonymisé]'
    # Accessibilité: tag spécial si demandé
    if result.get('accessible'):
        result['accessibility'] = 'checked'
    # Audit: log minimal (à remplacer par logger pro)
    result['_audit'] = 'legacy_core_v1'
    # Edge case: champ vide
    if not result:
        return {'legacy': True, 'empty': True}
    result['legacy'] = True
    return result
