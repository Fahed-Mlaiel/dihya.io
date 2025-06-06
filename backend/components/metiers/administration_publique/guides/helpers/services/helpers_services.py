# guides/helpers/helpers_services.py – Helpers avancés pour guides services

def validate_service_config(config):
    # Validation avancée de la config service
    if not isinstance(config, dict):
        raise ValueError('Config service invalide')
    if 'name' not in config or 'endpoint' not in config:
        raise ValueError('Nom et endpoint requis')
    return True

# helpers_services.py – Helpers ultra avancés services (Python)
def check_service(data):
    """Vérifie la conformité d’un service (statut, uptime)."""
    return data.get('status') == 'ok' and data.get('uptime', 0) > 90

def audit_service(data):
    """Audit de service, retourne score et conformité."""
    score = 0
    if data.get('status') == 'ok':
        score += 50
    if data.get('uptime', 0) > 90:
        score += 50
    return {'score': score, 'compliant': score == 100}
