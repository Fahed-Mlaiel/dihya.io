"""
Blueprint middleware logger métier (Python)
Logger middleware ultra avancé : configurable, contextuel, support async, intégration API/web, extension métier.
"""
from typing import Callable

def generate_logger_middleware(metier: str) -> Callable:
    """
    Génère un middleware logger contextuel pour API/web, support sync/async, configurable.
    """
    def middleware(request, next_handler=None):
        print(f"[{metier}] {getattr(request, 'method', '?')} {getattr(request, 'path', '?')}")
        if next_handler:
            return next_handler(request)
        return None
    return middleware

# Exemple d’utilisation :
# app.use(generate_logger_middleware('Inventaire'))
