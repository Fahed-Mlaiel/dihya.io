"""
Point d'entrée principal pour lancer l'application Flask Dihya Coding.
- Charge la configuration centralisée (sécurité, RGPD, plugins, multi-environnement)
- Initialise l'app, les extensions, les plugins et les blueprints métiers
- Active la gestion des logs, la sécurité avancée, la conformité RGPD
- Lance le serveur en mode sécurisé et extensible
"""

import os
from app import create_app

def main():
    print("[DEBUG] Starte Dihya Backend...")
    try:
        # Charge la configuration depuis la variable d'environnement ou par défaut
        config_path = os.environ.get("DIHYA_CONFIG", "backend.config.Config")
        print(f"[DEBUG] Verwende Konfiguration: {config_path}")
        app = create_app(config_path)
        print("[DEBUG] App initialisiert, starte Server...")

        # Affiche un résumé de l'environnement au démarrage (audit, debug)
        print(f"🚀 Dihya Coding Backend lancé sur {os.environ.get('ENV', 'development')}")
        print(f"🔒 Sécurité active | RGPD: {os.environ.get('RGPD_DELETE_ON_REQUEST', True)} | Plugins: {os.environ.get('PLUGINS_ENABLED', 'aucun')}")
        print(f"🌍 URL: {os.environ.get('BASE_URL', 'http://localhost:5000')}")

        # Port configurable (par défaut 5000)
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port, debug=True)
    except Exception as e:
        import traceback
        print("[ERREUR] Impossible de démarrer le backend Dihya :")
        print(e)
        traceback.print_exc()

if __name__ == "__main__":
    main()
