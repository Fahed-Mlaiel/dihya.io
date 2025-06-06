# services_environnement.py – Fixtures avancés de services d'environnement
# Respecte la conformité RGPD, la modularité et la logique métier

services = [
    {
        "id": "service-001",
        "name": "Service Test",
        "status": "ok",
        "environment": "production",
        "compliance": {"rgpd": True, "audit": True},
        "last_checked": "2025-06-05T00:00:00Z"
    },
    {
        "id": "service-002",
        "name": "Service Secondaire",
        "status": "maintenance",
        "environment": "staging",
        "compliance": {"rgpd": False, "audit": False},
        "last_checked": "2025-06-05T00:00:00Z"
    }
]
