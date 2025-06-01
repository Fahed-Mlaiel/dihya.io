"""
Dihya – Django Voyage API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour offres, destinations, réservations, itinéraires, avis, guides, événements, partenaires, IA voyage, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST voyage (sécurité, multilingue, souveraineté)
🇬🇧 Django REST travel routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للسفر (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n ugharas (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'offres', views.OffreViewSet, basename='offre')
router.register(r'destinations', views.DestinationViewSet, basename='destination')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'itineraires', views.ItineraireViewSet, basename='itineraire')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'guides', views.GuideViewSet, basename='guide')
router.register(r'evenements', views.EvenementViewSet, basename='evenement')
router.register(r'partenaires', views.PartenairesViewSet, basename='partenaire')
router.register(r'ia', views.IAVoyageViewSet, basename='ia-voyage')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'logs', views.LogVoyageViewSet, basename='log-voyage')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
