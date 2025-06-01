"""
Dihya – Django Services à la Personne API Routes Ultra Avancé
-------------------------------------------------------------
- Endpoints REST pour clients, intervenants, prestations, plannings, réservations, factures, avis, IA services, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST services à la personne (sécurité, multilingue, souveraineté)
🇬🇧 Django REST personal services routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST لخدمات الأشخاص (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n imdanen n umdan (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename='client')
router.register(r'intervenants', views.IntervenantViewSet, basename='intervenant')
router.register(r'prestations', views.PrestationViewSet, basename='prestation')
router.register(r'plannings', views.PlanningViewSet, basename='planning')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'factures', views.FactureViewSet, basename='facture')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'ia', views.IAServicesViewSet, basename='ia-services')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
