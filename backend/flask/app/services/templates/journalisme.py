"""
Template métier journalisme ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Journalisme", "en": "Journalism Project"},
        "description": {
            "fr": "Template journalisme sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant journalism template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["articles", "auteurs", "publications", "commentaires", "abonnés"],
        "plugins": ["auth", "audit", "publication"],
        "roles": ["admin", "rédacteur", "lecteur", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
