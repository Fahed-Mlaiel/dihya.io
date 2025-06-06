"""
Dihya – AI Backend Entrypoint (Python/Flask)
- Point d'entrée unique pour le moteur IA Python (multi-stack, multilingue, souveraineté, sécurité)
- Démarre l'API Flask IA ultra avancée (voir ai.py)
"""
import os
from flask import Flask
from .ai import ai_bp

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # UTF-8 pour multilingue
    app.register_blueprint(ai_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=bool(os.environ.get("DEBUG", False)))
