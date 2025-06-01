"""
Module 3D/VR/AR/IA pour Dihya Coding
Gestion avancée de projets immersifs, assets, IA, multitenancy, sécurité, i18n, plugins.
Compatible REST, GraphQL, plugins IA open source, audit, RGPD.
"""
from flask import Blueprint
from .template import register_3d_routes, bp_3d

# Enregistrement des routes métier 3D/VR/AR/IA
register_3d_routes(bp_3d)

__all__ = ["bp_3d"]
