"""
Template métier banque & finance ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Banque & Finance", "en": "Banking & Finance Project"},
        "description": {
            "fr": "Template banque/finance sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant banking/finance template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["comptes", "opérations", "clients", "virements", "crédits", "notifications"],
        "plugins": ["auth", "audit", "scoring", "analytics"],
        "roles": ["admin", "conseiller", "client", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
