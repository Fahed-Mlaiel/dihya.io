"""
Initialisation du module de documentation backend pour Dihya Coding.

Ce package centralise l’exposition et la gestion de la documentation API (OpenAPI/Swagger),
permettant la consultation interactive et sécurisée des spécifications de l’API.

Bonnes pratiques :
- Importer ici le blueprint principal (openapi_bp)
- Ne jamais exposer d’informations sensibles dans la documentation
- Sécuriser l’accès à la doc en production (auth, IP whitelist, etc.)
- Prévoir l’extensibilité pour la doc dynamique, le versionnage, etc.
- Documenter chaque endpoint ou ressource exposée

Exemple d’intégration :
    from backend.flask.app.docs import openapi_bp
    app.register_blueprint(openapi_bp)
"""

from .serve_openapi import openapi_bp