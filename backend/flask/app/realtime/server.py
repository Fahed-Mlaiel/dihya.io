"""
Serveur Flask-SocketIO pour la gestion du temps réel (WebSockets) dans Dihya Coding.

Ce module initialise l’instance SocketIO, configure la sécurité (CORS, authentification JWT),
et enregistre les événements temps réel via le module events.py.

Bonnes pratiques :
- Sécuriser les connexions WebSocket (CORS, authentification).
- Logger chaque connexion/déconnexion et événement critique.
- Ne jamais exposer de secrets ou d’informations sensibles via WebSocket.
- Documenter la configuration et les handlers.

Exemple d’utilisation :
    from backend.flask.app.realtime.server import socketio
    socketio.run(app, host="0.0.0.0", port=5000)
"""

from flask_socketio import SocketIO
from flask import Flask
from backend.flask.app.realtime.events import register_socketio_events

def create_socketio(app: Flask) -> SocketIO:
    """
    Initialise et configure SocketIO pour l’application Flask.
    :param app: instance Flask
    :return: instance SocketIO
    """
    socketio = SocketIO(
        app,
        cors_allowed_origins="*",
        logger=True,
        engineio_logger=True,
        async_mode="eventlet"  # ou "gevent" selon l’infra
    )
    register_socketio_events(socketio)
    return socketio

# Exemple d’exécution autonome
if __name__ == "__main__":
    from app import create_app  # Assure-toi que create_app existe
    app = create_app()
    socketio = create_socketio(app)
    socketio.run(app, host="0.0.0.0", port=5000)