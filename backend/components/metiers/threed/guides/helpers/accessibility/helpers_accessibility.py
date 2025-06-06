# guides/helpers/helpers_accessibility.py – Helpers avancés pour guides accessibilité

def validate_accessibility_config(config):
    # Validation avancée de la config accessibilité
    if not isinstance(config, dict):
        raise ValueError('Config accessibilité invalide')
    if 'level' not in config or config['level'] not in ['A','AA','AAA']:
        raise ValueError('Niveau WCAG requis')
    return True

# helpers_accessibility.py – Helpers ultra avancés accessibilité (Python)
def check_accessibility(data):
    """Vérifie la conformité accessibilité (contraste, navigation clavier)."""
    return data.get('contrast', 0) >= 7 and data.get('keyboard', False)

def audit_accessibility(data):
    """Audit d’accessibilité, retourne score et conformité."""
    score = 0
    if data.get('contrast', 0) >= 7:
        score += 50
    if data.get('keyboard', False):
        score += 50
    return {'score': score, 'compliant': score == 100}
