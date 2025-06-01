"""
Dihya – Tâches asynchrones pour Transport
- Notifications, IA, génération de rapports, gestion planning
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_conducteur(conducteur_id, message):
    # TODO: Envoyer notification (mail, push) au conducteur
    pass

@shared_task
def tache_rapport_trajets():
    # TODO: Générer rapport PDF/CSV des trajets
    pass
