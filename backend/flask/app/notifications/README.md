# notifications/ — Gestion centralisée des notifications (Dihya Coding)

Ce dossier regroupe la déclaration, l’envoi et la gestion des notifications pour le backend Flask Dihya Coding.

## Objectif

- Centraliser la logique d’envoi de notifications (email, push, SMS, etc.).
- Garantir la fiabilité, la sécurité et la traçabilité des communications avec les utilisateurs.
- Faciliter l’extension à de nouveaux canaux de notification.

## Bonnes pratiques

- Déclarer chaque canal de notification dans un fichier dédié (`email.py`, `push.py`, `sms.py`, etc.).
- Valider et filtrer les contenus envoyés pour éviter les injections ou abus.
- Logger chaque notification envoyée pour audit et conformité.
- Protéger les fonctions critiques par des vérifications de permissions.
- Prévoir des tests unitaires pour chaque canal de notification.
- Respecter la confidentialité et la conformité RGPD (ne jamais exposer d’informations sensibles).

## Exemple de structure

- `email.py` : envoi d’e-mails transactionnels ou marketing.
- `push.py` : notifications push (web, mobile).
- `sms.py` : notifications par SMS.
- `tests/` : tests unitaires pour chaque canal.

## Exemple d’utilisation

```python
from app.notifications.email import send_notification_email
from app.notifications.push import send_push_notification

send_notification_email("user@example.com", "Bienvenue sur Dihya Coding !")
send_push_notification(user_id, "Votre projet est prêt.")