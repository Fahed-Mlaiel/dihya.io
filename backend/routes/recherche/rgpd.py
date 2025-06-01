"""
RGPD ultra avancé pour Recherche (Django routes)
Anonymisation, export, conformité, hooks métier RGPD.
"""
def anonymize_project(project):
    project.name = '***'
    project.description = '***'
    return project
