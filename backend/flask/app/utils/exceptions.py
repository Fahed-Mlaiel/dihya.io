"""
Exceptions personnalisées pour Dihya Coding.

Ce module centralise les exceptions métier utilisées dans le backend.
Il permet une gestion claire, sécurisée et documentée des erreurs applicatives.

Bonnes pratiques :
- Ne jamais inclure de données sensibles dans les messages d’exception.
- Utiliser des codes d’erreur et messages explicites pour l’API.
- Logger chaque exception critique pour audit.
- Étendre les exceptions selon les besoins métier (validation, sécurité, quotas, etc.).

Exemple d’utilisation :
    from backend.flask.app.utils.exceptions import ValidationError
    raise ValidationError("Champ email invalide.")
"""

class DihyaError(Exception):
    """Exception de base pour Dihya Coding."""
    def __init__(self, message="Erreur interne Dihya Coding", code=500):
        super().__init__(message)
        self.code = code

class ValidationError(DihyaError):
    """Erreur de validation des données utilisateur."""
    def __init__(self, message="Erreur de validation", code=422):
        super().__init__(message, code)

class AuthError(DihyaError):
    """Erreur d’authentification ou d’autorisation."""
    def __init__(self, message="Authentification requise", code=401):
        super().__init__(message, code)

class PermissionError(DihyaError):
    """Erreur de permission insuffisante."""
    def __init__(self, message="Permission refusée", code=403):
        super().__init__(message, code)

class QuotaExceededError(DihyaError):
    """Erreur de quota IA ou API dépassé."""
    def __init__(self, message="Quota dépassé", code=429):
        super().__init__(message, code)

class NotFoundError(DihyaError):
    """Erreur ressource non trouvée."""
    def __init__(self, message="Ressource non trouvée", code=404):
        super().__init__(message, code)