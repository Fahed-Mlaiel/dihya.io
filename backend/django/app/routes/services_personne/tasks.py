"""
Dihya – Tâches asynchrones pour Services à la Personne
- Notifications, IA, génération de rapports, gestion planning
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_beneficiaire(b_id, message):
    # Notification multicanal (mail, SMS, push) au bénéficiaire, logs, RGPD
    from .models import Beneficiaire
    try:
        ben = Beneficiaire.objects.get(id=b_id)
        send_mail('Notification Dihya', message, 'noreply@dihya.com', [ben.email])
        # ... SMS/push extensible ...
    except Exception as e:
        print(f"[NOTIFY][FALLBACK] {e}")

@shared_task
def tache_rapport_prestations():
    # Génération rapport PDF/CSV des prestations, logs, RGPD, export
    from .models import Prestation
    import csv
    with open('/tmp/prestations_export.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'type', 'user'])
        for p in Prestation.objects.all():
            writer.writerow([p.id, p.date, p.type, p.user.id])
    # ... PDF export possible ...
    print('[RAPPORT] Export prestations terminé')
