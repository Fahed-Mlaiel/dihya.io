"""
Template métier BTP ultra avancé – Dihya Coding
Production-ready, sécurité, RGPD, audit, accessibilité, multitenancy, plugins, i18n, CI/CD, documentation, tests, souveraineté logicielle.
"""
def get_template():
    return {
        "name": {"fr": "Projet BTP", "en": "Construction & Public Works Project"},
        "description": {
            "fr": "Template BTP sécurisé, modulaire, multitenant, plugins, audit, RGPD, accessibilité.",
            "en": "Secure, modular, multitenant construction & public works template with plugins, audit, GDPR, accessibility."
        },
        "modules": ["chantiers", "équipes", "matériel", "fournisseurs", "finances"],
        "plugins": ["auth", "audit", "planning"],
        "roles": ["admin", "chef_chantier", "ouvrier", "auditeur"],
        "i18n": True,
        "audit": True,
        "accessibility": True,
        "rgpd": True,
        "multitenancy": True,
        "version": "1.0.0",
        "created_at": "2025-05-31"
    }
