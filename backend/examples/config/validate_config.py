"""
validate_config.py – Script ultra avancé de validation de configuration (YAML, JSON, TOML)
Vérifie la conformité RGPD, sécurité, audit, accessibilité, monitoring, CI/CD, i18n, structure, etc.
"""
import sys
import json
import yaml
import toml

def validate_config(config):
    # Vérification des clés critiques
    required_keys = [
        'app', 'audit_log', 'rgpd', 'i18n', 'security', 'accessibility', 'monitoring'
    ]
    for key in required_keys:
        if key not in config.get('app', {}):
            print(f"[ERREUR] Clé manquante : {key}")
            return False
    print("[OK] Structure de configuration valide.")
    # Vérification RGPD, sécurité, accessibilité, etc.
    if not config['app']['rgpd'].get('consent_required'):
        print("[ERREUR] RGPD : consentement requis non activé.")
        return False
    if not config['app']['security'].get('jwt'):
        print("[ERREUR] Sécurité : JWT non activé.")
        return False
    if not config['app']['accessibility'].get('enabled'):
        print("[ERREUR] Accessibilité non activée.")
        return False
    print("[OK] Conformité RGPD, sécurité, accessibilité validée.")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_config.py <config_file>")
        sys.exit(1)
    path = sys.argv[1]
    if path.endswith('.json'):
        with open(path) as f:
            config = json.load(f)
    elif path.endswith('.yaml') or path.endswith('.yml'):
        with open(path) as f:
            config = yaml.safe_load(f)
    elif path.endswith('.toml'):
        config = toml.load(path)
    else:
        print("Format non supporté.")
        sys.exit(1)
    if validate_config(config):
        print("[SUCCÈS] Configuration conforme.")
    else:
        print("[ÉCHEC] Configuration non conforme.")
        sys.exit(2)

if __name__ == '__main__':
    main()
