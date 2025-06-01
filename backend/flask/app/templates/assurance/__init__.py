"""
Module Assurance pour Dihya Coding
Gestion avancée des contrats, clients, sinistres, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_assurance_routes, bp_assurance

register_assurance_routes(bp_assurance)

blueprint = bp_assurance

__all__ = ["bp_assurance"]
