"""
Module Beauté pour Dihya Coding
Gestion avancée des salons, rendez-vous, prestations, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_beaute_routes, bp_beaute

register_beaute_routes(bp_beaute)

__all__ = ["bp_beaute"]
