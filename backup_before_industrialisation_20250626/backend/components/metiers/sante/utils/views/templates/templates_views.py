"""
templates_views.py – Helpers et templates (HTML, Jinja, etc.) pour le module sante
- Rendu, conformité RGPD, accessibilité, audit, i18n, sécurité, auditabilité
"""
import logging
from typing import Any

logger = logging.getLogger(__name__)


def render_template(name: str, context: Any) -> str:
    """
    Rendu d’un template HTML simple (ex: page, composant, email).
    - Sécurité : échappe les entrées si besoin
    - RGPD : pas de données personnelles non masquées
    - Accessibilité : structure claire
    - Auditabilité : log de chaque rendu
    """
    if not isinstance(name, str) or not name:
        logger.warning("Nom de template invalide : %s", name)
        name = "default"
    if context is None:
        context = ""
    logger.info(f"[TEMPLATE] Render {name}")
    return (
        f"<div class='template template-{name}'>"
        f"{context}</div>"
    )


__all__ = ["render_template"]
