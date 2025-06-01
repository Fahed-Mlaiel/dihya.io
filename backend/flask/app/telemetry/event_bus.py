"""
Event Bus – Dihya Coding

Ce module fournit un bus d’événements interne pour la centralisation des logs, traces, métriques et événements métier.
Il permet de publier, souscrire et traiter des événements de façon asynchrone et traçable.

Bonnes pratiques :
- Utiliser le bus pour toute notification ou événement transverse (audit, monitoring, sécurité…)
- Logger chaque événement critique pour auditabilité
- Valider le format des événements avant publication
- Ne jamais inclure de données sensibles dans les payloads d’événements
"""

import threading
from typing import Callable, Dict, List, Any
import logging

logger = logging.getLogger("dihya.telemetry.event_bus")
logger.setLevel(logging.INFO)

class Event:
    """
    Représente un événement métier ou technique.

    Attributes:
        name (str): Nom de l’événement.
        payload (dict): Données associées à l’événement.
    """
    def __init__(self, name: str, payload: Dict[str, Any]):
        self.name = name
        self.payload = payload

class EventBus:
    """
    Bus d’événements simple (in-process) pour la plateforme Dihya Coding.

    Usage :
        bus = EventBus()
        bus.subscribe("user_registered", handler)
        bus.publish("user_registered", {"user_id": 42})
    """
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Event], None]]] = {}
        self._lock = threading.Lock()

    def subscribe(self, event_name: str, handler: Callable[[Event], None]) -> None:
        """
        Abonne un handler à un événement.

        Args:
            event_name (str): Nom de l’événement.
            handler (callable): Fonction à appeler lors de la publication.
        """
        with self._lock:
            if event_name not in self._subscribers:
                self._subscribers[event_name] = []
            self._subscribers[event_name].append(handler)
            logger.info(f"Handler abonné à l’événement '{event_name}'.")

    def publish(self, event_name: str, payload: Dict[str, Any]) -> None:
        """
        Publie un événement à tous les handlers abonnés.

        Args:
            event_name (str): Nom de l’événement.
            payload (dict): Données associées à l’événement.
        """
        event = Event(event_name, payload)
        handlers = []
        with self._lock:
            handlers = list(self._subscribers.get(event_name, []))
        logger.info(f"Événement publié : {event_name} | Payload : {payload}")
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                logger.error(f"Erreur dans le handler de '{event_name}': {e}")

# Exemple d’utilisation (à retirer en production)
if __name__ == "__main__":
    def log_event(event: Event):
        print(f"[EVENT] {event.name} - {event.payload}")

    bus = EventBus()
    bus.subscribe("user_registered", log_event)
    bus.publish("user_registered", {"user_id": 123, "email": "user@example.com"})