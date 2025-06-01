"""
Dihya – Django Loisirs API Routes Ultra Avancé
----------------------------------------------
- Endpoints REST pour activités, événements, réservations, lieux, participants, avis, promotions, IA recommandation, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST loisirs (sécurité, multilingue, souveraineté)
🇬🇧 Django REST leisure routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للترفيه (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n lḥanaya (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'activites', views.ActiviteViewSet, basename='activite')
router.register(r'evenements', views.EvenementViewSet, basename='evenement')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'lieux', views.LieuViewSet, basename='lieu')
router.register(r'participants', views.ParticipantViewSet, basename='participant')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'promotions', views.PromotionViewSet, basename='promotion')
router.register(r'ia', views.IARecommandationViewSet, basename='ia-recommandation')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
