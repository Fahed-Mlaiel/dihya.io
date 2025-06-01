"""
Dihya – Django SEO API Routes Ultra Avancé
------------------------------------------
- Endpoints REST pour métadonnées, sitemaps, robots.txt, performance, accessibilité, IA SEO, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST SEO (sécurité, multilingue, souveraineté)
🇬🇧 Django REST SEO routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للسيو (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n SEO (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'metadonnees', views.MetaDonneeViewSet, basename='metadonnee')
router.register(r'sitemaps', views.SiteMapViewSet, basename='sitemap')
router.register(r'robots', views.RobotsTxtViewSet, basename='robots')
router.register(r'performance', views.PerformanceViewSet, basename='performance')
router.register(r'accessibilite', views.AccessibiliteViewSet, basename='accessibilite')
router.register(r'ia', views.IASEOViewSet, basename='ia-seo')
router.register(r'logs', views.LogSEOViewSet, basename='log-seo')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
