"""
RGPD ultra avancé pour Gamer (Django routes)
Anonymisation, export, conformité, hooks métier RGPD.
"""
def anonymize_project(project):
    project.name = '***'
    project.description = '***'
    return project
