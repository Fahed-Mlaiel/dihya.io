"""
Middleware d’authentification avancée pour le module threed.
"""


def authenticate_request(request):
    # Logique d’authentification métier
    user = getattr(request, "user", None)
    if not user or not user.is_authenticated:
        raise PermissionError("Authentification requise")
    return True
