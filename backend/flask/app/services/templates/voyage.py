"""
Template métier voyage ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Voyage", "en": "Travel Project"},
        "description": {
            "fr": "Template voyage sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant travel template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["circuits", "réservations", "clients", "guides", "hébergements"],
        "plugins": ["auth", "audit", "reservation"],
        "roles": ["admin", "guide", "voyageur", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
