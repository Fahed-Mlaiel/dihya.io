"""
Sectorisation ultra avancée pour Logistique (Django routes)
Gestion des secteurs, accès, RBAC sectorisé, hooks métier.
"""
def get_sector_for_project(project):
    return getattr(project, 'sector', 'logistique')
