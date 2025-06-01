"""
Mapping dynamique des routes métiers Dihya
Inclut sécurité, i18n, multitenancy, plugins, RGPD, audit, SEO, IA fallback.
"""
from typing import Dict, Any

METIERS_ROUTES_MAP: Dict[str, Dict[str, Any]] = {
    "manufacturing": {
        "rest": "/manufacturing",
        "graphql": "/manufacturing/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "marketing": {
        "rest": "/marketing",
        "graphql": "/marketing/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "medias": {
        "rest": "/medias",
        "graphql": "/medias/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "mobile": {
        "rest": "/mobile",
        "graphql": "/mobile/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "mode": {
        "rest": "/mode",
        "graphql": "/mode/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "preview": {
        "rest": "/preview",
        "graphql": "/preview/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "publicite": {
        "rest": "/publicite",
        "graphql": "/publicite/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    },
    "recherche": {
        "rest": "/recherche",
        "graphql": "/recherche/graphql",
        "security": True,
        "i18n": True,
        "multitenancy": True,
        "plugins": True,
        "rgpd": True,
        "seo": True,
        "ia_fallback": True
    }
}

def get_metier_route(metier: str, route_type: str = "rest") -> str:
    """Retourne la route REST ou GraphQL pour un métier donné."""
    return METIERS_ROUTES_MAP.get(metier, {}).get(route_type, "")
