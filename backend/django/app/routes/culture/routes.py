"""
Dihya – Django Culture API Routes Ultra Avancé
----------------------------------------------
- Endpoints REST pour événements, lieux, patrimoines, artistes, œuvres, réservations, IA, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST culture (sécurité, multilingue, souveraineté)
🇬🇧 Django REST culture routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للثقافة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tamedyazt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'evenements', views.EvenementViewSet, basename='evenement')
router.register(r'lieux', views.LieuViewSet, basename='lieu')
router.register(r'patrimoines', views.PatrimoineViewSet, basename='patrimoine')
router.register(r'artistes', views.ArtisteViewSet, basename='artiste')
router.register(r'oeuvres', views.OeuvreViewSet, basename='oeuvre')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'ia', views.IARecommandationViewSet, basename='ia-recommandation')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
