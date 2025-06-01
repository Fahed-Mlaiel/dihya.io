"""
Template métier santé ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet Santé", "en": "Health Project"},
        "description": {
            "fr": "Template santé sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant health template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["patients", "consultations", "praticiens", "rdv", "factures"],
        "plugins": ["auth", "audit", "rdv"],
        "roles": ["admin", "praticien", "patient", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
