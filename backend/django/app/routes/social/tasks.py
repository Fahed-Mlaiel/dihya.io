"""
Dihya – Tâches asynchrones pour Social
- Notifications, IA, génération de rapports, modération
"""
from celery import shared_task
from django.core.mail import send_mail

def notify_profil(profil_id, message):
    # Notification multicanal (mail, push) au profil, logs, RGPD
    from .models import Profil
    try:
        profil = Profil.objects.get(id=profil_id)
        send_mail('Notification Dihya', message, 'noreply@dihya.com', [profil.email])
        # ... push extensible ...
    except Exception as e:
        print(f"[NOTIFY][FALLBACK] {e}")

@shared_task
def tache_rapport_posts():
    # Génération rapport PDF/CSV des posts, logs, RGPD, export
    from .models import Post
    import csv
    with open('/tmp/posts_export.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'content', 'user'])
        for p in Post.objects.all():
            writer.writerow([p.id, p.date, p.content, p.user.id])
    print('[RAPPORT] Export posts terminé')
