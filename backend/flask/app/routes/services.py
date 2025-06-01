"""
Services transverses globaux pour toutes les routes Dihya (Flask).
Inclut sécurité, RGPD, accessibilité, plugins, audit, i18n, CI/CD, production-ready.
"""

from .schemas import *
from .validators import *
from .plugins import *
from .audit import log_audit_event
from .i18n import translate

__all__ = [
    "get_status",
    "get_error_response",
    "get_paginated_response",
]

def get_status():
    return {"status": "ok", "message": translate("success")}

def get_error_response(code, message, details=None, lang="fr"):
    return {"code": code, "message": translate(message, lang), "details": details}

def get_paginated_response(data, page, per_page, total):
    return {
        "data": data,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total
        }
    }
