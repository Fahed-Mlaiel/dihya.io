"""
Dihya – AI Backend Entrypoint (Python/Flask)
--------------------------------------------
- Point d'entrée unique pour le moteur IA Python (multi-stack, multilingue, souveraineté, sécurité)
- Démarre l'API Flask IA ultra avancée (voir ai.py)
- Prêt pour intégration, CI/CD, Codespaces, cloud souverain, audit RGPD/NIS2
- Documentation multilingue, RBAC, logs, fallback IA open source

🇫🇷 Point d'entrée backend IA Python (sécurité, fallback, multilingue)
🇬🇧 Python AI backend entry point (secure, fallback, multilingual)
🇦🇪 نقطة دخول محرك الذكاء الاصطناعي (Python) مع الأمان والدعم متعدد اللغات
ⵣ Amuddu n backend IA Python (amatu, fallback, multilingual)
"""

import os
from flask import Flask
from Dihya.backend.ai.ai import ai_bp

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # UTF-8 pour multilingue
    app.register_blueprint(ai_bp)
    # Sécurité, logs, RBAC, fallback IA open source, prêt CI/CD, Codespaces, production
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=bool(os.environ.get("DEBUG", False)))
