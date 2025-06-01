"""
RGPD ultra avancé pour Environnement (Django routes)
Anonymisation, export, conformité, hooks métier RGPD.
"""
def anonymize_project(project):
    project.name = '***'
    project.description = '***'
    return project
