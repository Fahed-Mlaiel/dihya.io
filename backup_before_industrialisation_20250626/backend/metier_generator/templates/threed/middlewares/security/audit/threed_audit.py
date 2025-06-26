"""
Middleware d’audit d’accès pour le module threed.
"""


def audit_access(request):
    print(f"[AUDIT] {getattr(request, 'user', None)} accède à {request.url}")
