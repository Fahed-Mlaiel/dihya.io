"""
Template réseau social pour Dihya Coding.

Inclut la structure de base, les routes, les modèles et les bonnes pratiques du secteur social.
Ce template sert de base à la génération automatique d’un projet de type réseau social.

Bonnes pratiques :
- Respecter la confidentialité et la sécurité des données utilisateurs.
- Prévoir des modèles extensibles (User, Post, Message, Comment, Notification).
- Documenter chaque composant du template.
- Ne jamais inclure de secrets ou de données sensibles dans le template.
- Prévoir des hooks pour l’extension (plugins, notifications, etc.).

Exemple d’utilisation :
    from backend.flask.app.services.templates.social import get_template
    template = get_template()
"""

def get_template():
    """
    Retourne la structure du template réseau social.
    :return: dict représentant le squelette du projet social
    """
    return {
        "routes": [
            "/posts", "/users", "/messages", "/feed", "/notifications"
        ],
        "models": [
            "User", "Post", "Message", "Comment", "Notification"
        ],
        "dependencies": [
            "sqlalchemy", "flask-login"
        ],
        "description": "Template réseau social prêt à l’emploi, extensible et sécurisé"
    }