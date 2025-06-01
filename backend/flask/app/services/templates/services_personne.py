"""
Template métier services à la personne ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Services à la Personne", "en": "Personal Services Project"},
        "description": {
            "fr": "Template services à la personne sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant personal services template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["prestations", "clients", "intervenants", "plannings", "factures"],
        "plugins": ["auth", "audit", "planning"],
        "roles": ["admin", "intervenant", "client", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
