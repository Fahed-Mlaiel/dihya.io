# guides/helpers/helpers_plugins.py – Helpers avancés pour guides plugins

def validate_plugin_config(config):
    # Validation avancée de la config plugin
    if not isinstance(config, dict):
        raise ValueError('Config plugin invalide')
    if 'name' not in config or 'version' not in config:
        raise ValueError('Nom et version requis')
    return True

# helpers_plugins.py – Helpers ultra avancés plugins (Python)
def check_plugin(data):
    """Vérifie la conformité d’un plugin (activé, version)."""
    return data.get('enabled', False) and bool(data.get('version'))

def audit_plugin(data):
    """Audit de plugin, retourne score et conformité."""
    score = 0
    if data.get('enabled', False):
        score += 50
    if data.get('version'):
        score += 50
    return {'score': score, 'compliant': score == 100}
