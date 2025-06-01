"""
Initialisation du module de gestion des tâches asynchrones pour Dihya Coding.

Ce package permet de centraliser la déclaration et l'import des tâches de fond (emails, notifications, génération, nettoyage, etc.)
pour une exécution asynchrone via Celery, RQ ou tout autre gestionnaire de tâches.

Bonnes pratiques :
- Déclarer chaque tâche dans un fichier dédié (ex : email_tasks.py, cleanup_tasks.py, generation_tasks.py).
- Protéger les tâches critiques par des vérifications de permissions et de sécurité.
- Documenter chaque tâche avec une docstring claire.
- Prévoir des tests unitaires pour chaque tâche.
- Ne jamais traiter de données sensibles sans chiffrement ou validation préalable.

Exemple d'import :
    from backend.flask.app.tasks.email_tasks import send_welcome_email
    from backend.flask.app.tasks.generation_tasks import generate_project_async
    from backend.flask.app.tasks.cleanup_tasks import cleanup_temp_files
"""

# Import des tâches principales pour exposition directe
# (décommentez selon les fichiers présents)
# from .email_tasks import send_welcome_email
# from .generation_tasks import generate_project_async
# from .cleanup_tasks import cleanup_temp_files