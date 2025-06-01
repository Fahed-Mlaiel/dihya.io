"""
Module Automobile pour Dihya Coding
Gestion avancée de flotte, entretiens, locations, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_automobile_routes, bp_automobile

register_automobile_routes(bp_automobile)

__all__ = ["bp_automobile"]
