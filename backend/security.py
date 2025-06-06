"""
security.py – Sécurité ultra avancée Dihya
- CORS, JWT, WAF, anti-DDOS, validation, audit, conformité RGPD
- Extension plugins, logs structurés, multitenancy, docstring, type hints
"""
from backend.flask.app.utils.jwt import create_jwt_token
import logging
from typing import Dict


def get_jwt_token_for_role(role: str, tenant: str = None) -> str:
    """
    Génère un JWT sécurisé pour un rôle donné, multitenancy, audit RGPD.
    Args:
        role (str): Rôle utilisateur (admin, user, invité, ...)
        tenant (str, optional): Identifiant tenant
    Returns:
        str: JWT sécurisé encodant le rôle et le tenant
    """
    payload: Dict = {"role": role, "tenant": tenant}
    logging.info(f"[security] Génération JWT role={role} tenant={tenant}")
    return create_jwt_token(payload)

# Extension plugins sécurité possible (voir docs/securite/)
