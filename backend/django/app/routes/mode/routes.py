"""
Dihya – Django Mode & Fashion API Routes Ultra Avancé
-----------------------------------------------------
- Endpoints REST pour collections, produits, créateurs, tendances, shootings, médias, avis, IA fashion, recommandations, modération, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, modération IA, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST mode (sécurité, multilingue, souveraineté)
🇬🇧 Django REST fashion routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للموضة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n lḥella (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'collections', views.CollectionViewSet, basename='collection')
router.register(r'produits', views.ProduitViewSet, basename='produit')
router.register(r'createurs', views.CreateurViewSet, basename='createur')
router.register(r'tendances', views.TendanceViewSet, basename='tendance')
router.register(r'shootings', views.ShootingViewSet, basename='shooting')
router.register(r'medias', views.MediaViewSet, basename='media')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'ia', views.IAFashionViewSet, basename='ia-fashion')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, modération IA, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
