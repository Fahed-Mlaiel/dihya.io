"""
Middleware de gestion de session pour le module threed.
"""


def session_context(request):
    session = getattr(request, "session", {})
    request.context = getattr(request, "context", {})
    request.context["session"] = session
    return request
