"""
Template éducation pour Dihya Coding.

Inclut la structure de base, les routes, les modèles et les bonnes pratiques du secteur éducatif.
Ce template sert de base à la génération automatique d’un projet de type plateforme éducative.

Bonnes pratiques :
- Respecter la confidentialité des données élèves/enseignants.
- Prévoir des modèles extensibles (Course, Student, Teacher, Assignment, Grade).
- Documenter chaque composant du template.
- Ne jamais inclure de secrets ou de données sensibles dans le template.
- Prévoir des hooks pour l’extension (plugins, notifications, etc.).

Exemple d’utilisation :
    from backend.flask.app.services.templates.education import get_template
    template = get_template()
"""

def get_template():
    """
    Retourne la structure du template éducation.
    :return: dict représentant le squelette du projet éducatif
    """
    return {
        "routes": [
            "/courses", "/students", "/teachers", "/assignments", "/grades"
        ],
        "models": [
            "Course", "Student", "Teacher", "Assignment", "Grade"
        ],
        "dependencies": [
            "sqlalchemy", "flask-login"
        ],
        "description": "Template éducation prêt à l’emploi, extensible et sécurisé"
    }