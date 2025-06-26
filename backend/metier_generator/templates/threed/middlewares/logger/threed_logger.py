"""
Middleware de logging avancé pour le métier threed.
"""


def log_request(request):
    print(f"[THREED] {request.method} {request.url}")
