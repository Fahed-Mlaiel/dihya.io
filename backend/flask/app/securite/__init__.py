"""
Initialisation du module sécurité avancée pour Dihya Coding.

Ce package regroupe les composants de sécurité transverses : gestion des accès, ACL, audit, vérification d’intégrité,
chiffrement, gestion des secrets, sécurité des tâches asynchrones, etc.

Bonnes pratiques :
- Centraliser ici toute la logique de sécurité réutilisable (ACL, audit, helpers de chiffrement…).
- Documenter chaque fonction et classe avec une docstring claire.
- Protéger les fonctions critiques par des vérifications de permissions et de contexte.
- Ne jamais stocker ou logguer de secrets en clair.
- Prévoir des tests unitaires pour chaque helper de sécurité.
- Respecter la conformité RGPD et les bonnes pratiques OWASP.

Exemple d’import :
    from backend.flask.app.securite.acl import check_access
    from backend.flask.app.securite.crypto import encrypt_data, decrypt_data
"""
from backend.flask.app.securite.acl import *
from backend.flask.app.securite.crypto import *
from backend.flask.app.securite.integrity import *
from backend.flask.app.securite.secrets import *
from backend.flask.app.securite.audit import *
