"""
Exceptions globales – Dihya Coding

Ce module centralise toutes les exceptions personnalisées utilisées dans le backend.
Il permet une gestion cohérente des erreurs, une meilleure traçabilité et une sécurité accrue.

Bonnes pratiques :
- Toujours hériter de DihyaBaseException pour les erreurs métier
- Documenter chaque exception
- Ne jamais exposer d’informations sensibles dans les messages d’erreur
"""

class DihyaBaseException(Exception):
    """Exception de base pour toutes les erreurs métier Dihya Coding."""
    pass

class ValidationError(DihyaBaseException):
    """Erreur de validation des données d’entrée."""
    def __init__(self, message="Erreur de validation des données."):
        super().__init__(message)

class AuthenticationError(DihyaBaseException):
    """Erreur d’authentification (JWT, OAuth, etc.)."""
    def __init__(self, message="Authentification requise ou invalide."):
        super().__init__(message)

class AuthorizationError(DihyaBaseException):
    """Erreur d’autorisation (accès refusé)."""
    def __init__(self, message="Vous n’avez pas les droits nécessaires pour cette action."):
        super().__init__(message)

class NotFoundError(DihyaBaseException):
    """Erreur ressource non trouvée."""
    def __init__(self, message="Ressource non trouvée."):
        super().__init__(message)

class ServiceUnavailableError(DihyaBaseException):
    """Erreur service externe indisponible (API, base de données, etc.)."""
    def __init__(self, message="Service temporairement indisponible."):
        super().__init__(message)

class RateLimitError(DihyaBaseException):
    """Erreur de dépassement de quota ou rate limiting."""
    def __init__(self, message="Trop de requêtes, veuillez réessayer plus tard."):
        super().__init__(message)