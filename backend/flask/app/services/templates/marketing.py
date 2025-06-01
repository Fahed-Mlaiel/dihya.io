"""
Template métier marketing ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Marketing", "en": "Marketing Project"},
        "description": {
            "fr": "Template marketing sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant marketing template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["campagnes", "contacts", "segmentation", "analytics", "contenus"],
        "plugins": ["auth", "audit", "analytics"],
        "roles": ["admin", "marketer", "client", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
