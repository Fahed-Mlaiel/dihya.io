"""
Template métier assurance ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Assurance", "en": "Insurance Project"},
        "description": {
            "fr": "Template assurance sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant insurance template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["contrats", "clients", "sinistres", "garanties", "paiements"],
        "plugins": ["auth", "audit", "paiement"],
        "roles": ["admin", "gestionnaire", "client", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
