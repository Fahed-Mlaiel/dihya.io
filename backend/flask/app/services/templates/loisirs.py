"""
Template métier loisirs ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Loisirs", "en": "Leisure Project"},
        "description": {
            "fr": "Template loisirs sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant leisure template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["activités", "clubs", "événements", "réservations", "participants"],
        "plugins": ["auth", "audit", "reservation"],
        "roles": ["admin", "organisateur", "participant", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
