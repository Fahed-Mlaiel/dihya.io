"""
Module Banque & Finance pour Dihya Coding
Gestion avancée des comptes, clients, opérations, crédits, sécurité, i18n, audit, RGPD.
Compatible REST, GraphQL, plugins, audit, multitenancy, export, SEO.
"""
from flask import Blueprint
from .template import register_banque_finance_routes, bp_banque_finance

register_banque_finance_routes(bp_banque_finance)

__all__ = ["bp_banque_finance"]
