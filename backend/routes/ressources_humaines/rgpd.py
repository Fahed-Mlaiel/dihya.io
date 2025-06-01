"""
RGPD ultra avancé pour Ressources Humaines (Django routes)
Anonymisation, export, conformité, hooks métier RGPD.
"""
def anonymize_project(project):
    project.name = '***'
    project.description = '***'
    return project
