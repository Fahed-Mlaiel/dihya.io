"""
Template métier science ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Science", "en": "Science Project"},
        "description": {
            "fr": "Template science sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant science template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["recherches", "publications", "équipes", "projets", "expériences"],
        "plugins": ["auth", "audit", "publication"],
        "roles": ["admin", "chercheur", "étudiant", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
