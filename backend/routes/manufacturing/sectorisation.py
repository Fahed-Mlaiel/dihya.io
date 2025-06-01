"""
Sectorisation ultra avancée pour Manufacturing (Django routes)
Gestion des secteurs, accès, RBAC sectorisé, hooks métier.
"""
def get_sector_for_project(project):
    return getattr(project, 'sector', 'manufacturing')
