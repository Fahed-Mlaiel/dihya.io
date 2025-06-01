"""
Module Administration Publique pour Dihya Coding
Gestion avancée des démarches, citoyens, agents, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_admin_publique_routes, bp_admin_publique

register_admin_publique_routes(bp_admin_publique)

__all__ = ["bp_admin_publique"]

blueprint = bp_admin_publique
