"""
Initialisation du module de gestion des tâches planifiées (scheduler) pour Dihya Coding.

Ce package centralise la déclaration, la planification et la gestion sécurisée des jobs périodiques ou différés
(cron jobs, tâches planifiées, maintenance automatique, etc.).

Bonnes pratiques :
- Déclarer chaque tâche planifiée dans un fichier dédié (ex : cleanup_jobs.py, report_jobs.py).
- Documenter chaque job avec une docstring claire (fréquence, but, sécurité).
- Protéger les jobs critiques par des vérifications de permissions et de contexte.
- Logger l’exécution, les succès et les erreurs pour audit et monitoring.
- Prévoir des tests unitaires pour chaque job planifié.
- Ne jamais traiter de données sensibles sans validation ou chiffrement préalable.
- Utiliser des outils robustes (APScheduler, Celery Beat, cron) pour la production.

Exemple d’import :
    from backend.flask.app.scheduler.cleanup_jobs import schedule_cleanup
    from backend.flask.app.scheduler.report_jobs import generate_daily_report
"""
# Exemple d’import automatique (à compléter selon les fichiers créés)
# from .cleanup_jobs import schedule_cleanup
# from .report_jobs import generate_daily_report