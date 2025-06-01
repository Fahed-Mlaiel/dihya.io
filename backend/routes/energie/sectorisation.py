"""
Sectorisation ultra avancée pour Energie (Django routes)
Gestion des secteurs, accès, RBAC sectorisé, hooks métier.
"""
def get_sector_for_project(project):
    # Stub: retourne le secteur métier du projet
    return getattr(project, 'sector', 'energie')
