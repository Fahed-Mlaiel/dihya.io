# guides/fallback/fallback_services.py – Fallbacks et tests avancés pour guides services

def fallback_service_config():
    # Fallback de configuration service pour tests d’intégration
    return {
        'name': 'service-fallback',
        'endpoint': '/api/fallback',
        'description': 'Fallback de test pour service',
    }
