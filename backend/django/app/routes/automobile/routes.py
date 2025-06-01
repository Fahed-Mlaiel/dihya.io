"""
Dihya – Django Automobile API Routes Ultra Avancé
-------------------------------------------------
- Endpoints REST pour véhicules, propriétaires, entretiens, sinistres, télématique, IoT, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST automobile (sécurité, multilingue, souveraineté)
🇬🇧 Django REST automobile routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للسيارات (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tigmmi n taggara (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'vehicules', views.VehiculeViewSet, basename='vehicule')
router.register(r'proprietaires', views.ProprietaireViewSet, basename='proprietaire')
router.register(r'entretiens', views.EntretienViewSet, basename='entretien')
router.register(r'sinistres', views.SinistreViewSet, basename='sinistre')
router.register(r'telematiques', views.TelematicViewSet, basename='telematique')
router.register(r'iot', views.IoTViewSet, basename='iot')
router.register(r'alertes', views.AlerteViewSet, basename='alerte')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
