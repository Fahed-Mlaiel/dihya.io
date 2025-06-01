"""
Constantes globales – Dihya Coding

Ce module centralise toutes les constantes réutilisables dans le backend :
rôles utilisateurs, statuts, politiques de sécurité, messages génériques, etc.

Bonnes pratiques :
- Ne jamais dupliquer une constante : la définir ici et l’importer partout
- Préfixer les constantes par leur domaine si besoin (ex : ROLE_, STATUS_)
- Documenter chaque constante importante
"""

# Rôles utilisateurs
ROLE_ADMIN = "admin"
ROLE_USER = "user"
ROLE_GUEST = "guest"

ALL_ROLES = [ROLE_ADMIN, ROLE_USER, ROLE_GUEST]

# Statuts de projet
STATUS_DRAFT = "draft"
STATUS_GENERATING = "generating"
STATUS_READY = "ready"
STATUS_FAILED = "failed"
STATUS_ARCHIVED = "archived"

ALL_PROJECT_STATUS = [
    STATUS_DRAFT,
    STATUS_GENERATING,
    STATUS_READY,
    STATUS_FAILED,
    STATUS_ARCHIVED
]

# Politiques de sécurité
PASSWORD_MIN_LENGTH = 8
PASSWORD_REQUIRE_UPPER = True
PASSWORD_REQUIRE_LOWER = True
PASSWORD_REQUIRE_DIGIT = True
PASSWORD_REQUIRE_SPECIAL = True

# Messages génériques (jamais d’info sensible)
MSG_ERROR_GENERIC = "Une erreur est survenue. Veuillez réessayer plus tard."
MSG_UNAUTHORIZED = "Accès non autorisé."
MSG_FORBIDDEN = "Action interdite."
MSG_NOT_FOUND = "Ressource non trouvée."

# Autres constantes globales
DEFAULT_LANGUAGE = "fr"
SUPPORTED_LANGUAGES = ["fr", "en", "ar", "tzm"]
JWT_ALGORITHM = "HS256"