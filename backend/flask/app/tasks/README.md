# tasks/ — Tâches asynchrones et jobs de fond (Dihya Coding)

Ce dossier centralise la déclaration, la documentation et la gestion des tâches asynchrones pour le backend Flask Dihya Coding.

## Objectif

- Permettre l’exécution de tâches longues ou différées (emails, notifications, génération, nettoyage, etc.) hors du thread principal.
- Faciliter l’intégration avec des gestionnaires de tâches comme Celery, RQ, Dramatiq, etc.
- Garantir la sécurité, la traçabilité et la robustesse des traitements de fond.

## Bonnes pratiques

- Déclarer chaque type de tâche dans un fichier dédié (`email_tasks.py`, `cleanup_tasks.py`, `generation_tasks.py`, etc.).
- Documenter chaque tâche avec une docstring claire (but, paramètres, sécurité).
- Protéger les tâches critiques par des vérifications de permissions et de sécurité.
- Ne jamais traiter de données sensibles sans chiffrement ou validation préalable.
- Prévoir des tests unitaires pour chaque tâche.
- Logger les erreurs et succès pour audit et monitoring.
- Utiliser des files de tâches robustes (Redis, RabbitMQ, etc.) pour la production.

## Exemple de structure

- `email_tasks.py` : envoi d’e-mails (bienvenue, notification, etc.)
- `cleanup_tasks.py` : nettoyage périodique des données obsolètes.
- `generation_tasks.py` : génération de rapports, de projets, etc.
- `notification_tasks.py` : envoi de notifications push, SMS, etc.
- `tests/` : tests unitaires pour chaque tâche.

## Exemple d’utilisation

```python
from app.tasks.email_tasks import send_welcome_email

# Appel synchrone (pour test)
send_welcome_email("user@example.com")

# Appel asynchrone (avec Celery)
send_welcome_email.delay("user@example.com")