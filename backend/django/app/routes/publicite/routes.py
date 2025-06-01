"""
Dihya – Django Publicité API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour campagnes, annonces, emplacements, audiences, budgets, analytics, IA publicité, A/B testing, notifications, rapports
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, modération IA, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST publicité (sécurité, multilingue, souveraineté)
🇬🇧 Django REST advertising routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للإعلانات (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n publicite (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'campagnes', views.CampagneViewSet, basename='campagne')
router.register(r'annonces', views.AnnonceViewSet, basename='annonce')
router.register(r'emplacements', views.EmplacementViewSet, basename='emplacement')
router.register(r'audiences', views.AudienceViewSet, basename='audience')
router.register(r'budgets', views.BudgetViewSet, basename='budget')
router.register(r'analytics', views.AnalyticsViewSet, basename='analytics')
router.register(r'abtesting', views.ABTestingViewSet, basename='abtesting')
router.register(r'ia', views.IAPubliciteViewSet, basename='ia-publicite')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, modération IA, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
