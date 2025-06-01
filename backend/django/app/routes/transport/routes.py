"""
Dihya – Django Transport API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour véhicules, trajets, horaires, réservations, tickets, flotte, chauffeurs, IA transport, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST transport (sécurité, multilingue, souveraineté)
🇬🇧 Django REST transport routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للنقل (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tamsalt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'vehicules', views.VehiculeViewSet, basename='vehicule')
router.register(r'trajets', views.TrajetViewSet, basename='trajet')
router.register(r'horaires', views.HoraireViewSet, basename='horaire')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'tickets', views.TicketViewSet, basename='ticket')
router.register(r'flotte', views.FlotteViewSet, basename='flotte')
router.register(r'chauffeurs', views.ChauffeurViewSet, basename='chauffeur')
router.register(r'ia', views.IATransportViewSet, basename='ia-transport')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'logs', views.LogTransportViewSet, basename='log-transport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
