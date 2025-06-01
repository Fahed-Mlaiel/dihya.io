"""
Module Arts pour Dihya Coding
Gestion avancée des événements, galeries, portfolios, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from .template import arts_bp

bp_arts = arts_bp
__all__ = ["arts_bp", "bp_arts"]
