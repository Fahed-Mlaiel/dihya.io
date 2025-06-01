"""
Template métier hôtellerie ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Hôtellerie", "en": "Hotel Project"},
        "description": {
            "fr": "Template hôtellerie sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant hotel template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["chambres", "réservations", "clients", "services", "factures"],
        "plugins": ["auth", "audit", "reservation"],
        "roles": ["admin", "réceptionniste", "client", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
