"""
Gestion des événements WebSocket (temps réel) pour Dihya Coding.

Ce module définit les handlers pour les événements temps réel (chat, notifications, collaboration, etc.)
via Flask-SocketIO. Il centralise la sécurité, la validation et la documentation des messages.

Bonnes pratiques :
- Authentifier chaque connexion (JWT, session).
- Valider et filtrer tous les messages entrants.
- Logger chaque événement critique avec horodatage (sans données sensibles).
- Ne jamais transmettre de secrets ou d’informations confidentielles via WebSocket.
- Documenter chaque événement supporté.

Exemple d’utilisation :
    from backend.flask.app.realtime.events import register_socketio_events
    register_socketio_events(socketio)
"""

from flask_jwt_extended import decode_token
from flask_socketio import emit, join_room, leave_room, disconnect
from datetime import datetime

def authenticate_socketio(sid, environ):
    """
    Authentifie la connexion WebSocket via JWT passé en query string.
    """
    token = environ.get('HTTP_SEC_WEBSOCKET_PROTOCOL')
    if not token:
        return False
    try:
        decode_token(token)
        return True
    except Exception:
        return False

def register_socketio_events(socketio):
    """
    Enregistre les handlers d’événements WebSocket sur l’instance SocketIO.
    """

    @socketio.on('connect')
    def handle_connect():
        # Authentification à la connexion (exemple simplifié)
        if not authenticate_socketio(request.sid, request.environ):
            emit('error', {'message': 'Authentification WebSocket requise.'})
            disconnect()
        else:
            emit('connected', {'message': 'Connexion WebSocket réussie.'})

    @socketio.on('join')
    def handle_join(data):
        """
        Handler pour rejoindre une room (ex: chat, projet).
        """
        room = data.get('room')
        if room:
            join_room(room)
            emit('joined', {'room': room}, room=room)
            log_event('join', room)
        else:
            emit('error', {'message': 'Room invalide.'})

    @socketio.on('leave')
    def handle_leave(data):
        """
        Handler pour quitter une room.
        """
        room = data.get('room')
        if room:
            leave_room(room)
            emit('left', {'room': room}, room=room)
            log_event('leave', room)
        else:
            emit('error', {'message': 'Room invalide.'})

    @socketio.on('message')
    def handle_message(data):
        """
        Handler pour envoyer un message à une room.
        """
        room = data.get('room')
        msg = data.get('message')
        if room and msg:
            emit('message', {'message': msg, 'timestamp': datetime.utcnow().isoformat()}, room=room)
            log_event('message', room, msg)
        else:
            emit('error', {'message': 'Message ou room manquant.'})

def log_event(event, room, details=""):
    """
    Logge un événement temps réel pour audit.
    """
    log_file = "logs/realtime.log"
    entry = f"{datetime.utcnow().isoformat()} | event={event} | room={room} | details={details}"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception:
        pass