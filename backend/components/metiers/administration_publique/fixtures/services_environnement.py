# Fixture de services pour tests Threed
services = [
    {
        "name": "Threed Service Test",
        "environment": "threed-test",
        "service": "threed",
        "description": "Service de test pour Threed",
        "type": "3d",
        "statut": "actif",
        "audit": {
            "rgpd": True,
            "plugins": ["plugin1", "plugin2"],
            "i18n": ["fr", "en", "de"]
        }
    },
    # ... autres services éventuels ...
]
