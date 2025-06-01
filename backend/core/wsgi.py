# WSGI entrypoint for Dihya Backend (ultra avancé, production-ready)
from .app import create_app, socketio

app = create_app()

if __name__ == "__main__":
    # Pour développement local :
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
