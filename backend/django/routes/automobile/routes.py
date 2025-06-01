"""
Dihya – Django Automobile API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour véhicules, modèles, marques, maintenance, logs, audit, IA, plugins
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST Automobile (sécurité, multilingue, souveraineté)
🇬🇧 Django REST Automobile routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للسيارات (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n Automobile (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'vehicules', views.VehiculeViewSet, basename='vehicule')
router.register(r'modeles', views.ModeleViewSet, basename='modele')
router.register(r'marques', views.MarqueViewSet, basename='marque')
router.register(r'maintenance', views.MaintenanceViewSet, basename='maintenance')
router.register(r'ia', views.IAAutomobileViewSet, basename='ia-automobile')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
