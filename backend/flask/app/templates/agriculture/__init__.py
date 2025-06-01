"""
Module Agriculture pour Dihya Coding
Gestion avancée des exploitations, cultures, stocks, météo, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_agriculture_routes, bp_agriculture

register_agriculture_routes(bp_agriculture)

blueprint = bp_agriculture

__all__ = ["bp_agriculture"]
