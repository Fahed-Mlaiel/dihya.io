"""
Dihya – Django Marketing API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour campagnes, leads, audiences, canaux, contenus, analytics, IA marketing, A/B testing, notifications, rapports
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST marketing (sécurité, multilingue, souveraineté)
🇬🇧 Django REST marketing routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للتسويق (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n marketing (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'campagnes', views.CampagneViewSet, basename='campagne')
router.register(r'leads', views.LeadViewSet, basename='lead')
router.register(r'audiences', views.AudienceViewSet, basename='audience')
router.register(r'canaux', views.CanalViewSet, basename='canal')
router.register(r'contenus', views.ContenuViewSet, basename='contenu')
router.register(r'analytics', views.AnalyticsViewSet, basename='analytics')
router.register(r'abtesting', views.ABTestingViewSet, basename='abtesting')
router.register(r'ia', views.IAMarketingViewSet, basename='ia-marketing')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
