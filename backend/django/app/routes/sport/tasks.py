"""
Dihya – Tâches asynchrones pour Sport
- Notifications, IA, génération de rapports, gestion planning
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_club(club_id, message):
    # TODO: Envoyer notification (mail, push) au club
    pass

@shared_task
def tache_rapport_resultats():
    # TODO: Générer rapport PDF/CSV des résultats
    pass
