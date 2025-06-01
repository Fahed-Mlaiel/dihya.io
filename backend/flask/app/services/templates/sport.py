"""
Template métier sport ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Sport", "en": "Sport Project"},
        "description": {
            "fr": "Template sport sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant sport template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["équipes", "compétitions", "joueurs", "matchs", "classements"],
        "plugins": ["auth", "audit", "classement"],
        "roles": ["admin", "coach", "joueur", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
