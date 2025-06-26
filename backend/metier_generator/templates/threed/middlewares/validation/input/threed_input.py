"""
Middleware de validation d’entrée pour le module threed.
"""


def validate_input(request):
    data = getattr(request, "data", {})
    if not data:
        raise ValueError("Aucune donnée fournie")
    return request
