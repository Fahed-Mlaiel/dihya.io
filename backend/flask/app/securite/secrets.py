"""
Gestion sécurisée des secrets pour Dihya Coding.

Ce module centralise la gestion, le chargement et la validation des secrets applicatifs (clés API, tokens, credentials, etc.)
pour garantir la sécurité, la traçabilité et la conformité RGPD.
"""

import os
from typing import Optional


class SecretNotFound(Exception):
    pass


def get_secret(name: str, default: Optional[str] = None, required: bool = True) -> str:
    value = os.environ.get(name, default)
    if required and (value is None or value == ""):
        raise SecretNotFound(f"Le secret '{name}' est requis mais n'est pas défini.")
    return value


def validate_secrets(required_secrets: list):
    for secret in required_secrets:
        get_secret(secret, required=True)
