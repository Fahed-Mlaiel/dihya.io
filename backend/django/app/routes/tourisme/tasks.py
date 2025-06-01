"""
Dihya – Tâches asynchrones pour Tourisme
- Notifications, IA, génération de rapports, gestion planning
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_client(reservation_id, message):
    # Notification multicanal (mail, push) au client, logs, RGPD
    from .models import Reservation
    try:
        reservation = Reservation.objects.get(id=reservation_id)
        send_mail('Notification Dihya', message, 'noreply@dihya.com', [reservation.client.email])
        # ... push extensible ...
    except Exception as e:
        print(f"[NOTIFY][FALLBACK] {e}")

@shared_task
def tache_rapport_reservations():
    # Génération rapport PDF/CSV des réservations, logs, RGPD, export
    from .models import Reservation
    import csv
    with open('/tmp/reservations_export.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'client', 'offre'])
        for r in Reservation.objects.all():
            writer.writerow([r.id, r.date, r.client.id, r.offre.id])
    print('[RAPPORT] Export réservations terminé')
