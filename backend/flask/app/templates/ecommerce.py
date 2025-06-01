"""
Template e-commerce pour Dihya Coding.

Inclut la structure de base, les routes, les modèles et les bonnes pratiques du secteur e-commerce.
Ce template sert de base à la génération automatique d’un projet de boutique en ligne.

Bonnes pratiques :
- Respecter la sécurité des paiements et la confidentialité des données clients.
- Prévoir des modèles extensibles (Product, Order, User, Cart, Payment).
- Documenter chaque composant du template.
- Ne jamais inclure de secrets ou de données sensibles dans le template.
- Prévoir des hooks pour l’extension (plugins, notifications, analytics, etc.).

Exemple d’utilisation :
    from backend.flask.app.services.templates.ecommerce import get_template
    template = get_template()
"""

def get_template():
    """
    Retourne la structure du template e-commerce.
    :return: dict représentant le squelette du projet e-commerce
    """
    return {
        "routes": [
            "/products", "/cart", "/checkout", "/orders", "/payments"
        ],
        "models": [
            "Product", "Order", "User", "Cart", "Payment"
        ],
        "dependencies": [
            "sqlalchemy", "stripe", "flask-login"
        ],
        "description": "Template e-commerce prêt à l’emploi, extensible et sécurisé"
    }