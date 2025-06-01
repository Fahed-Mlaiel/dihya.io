"""
Dihya – Django Arts API Routes Ultra Avancé
-------------------------------------------
- Endpoints REST pour œuvres, artistes, expositions, galeries, NFT, IA générative, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST arts (sécurité, multilingue, souveraineté)
🇬🇧 Django REST arts routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للفنون (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'oeuvres', views.OeuvreViewSet, basename='oeuvre')
router.register(r'artistes', views.ArtisteViewSet, basename='artiste')
router.register(r'expositions', views.ExpositionViewSet, basename='exposition')
router.register(r'galeries', views.GalerieViewSet, basename='galerie')
router.register(r'nft', views.NFTViewSet, basename='nft')
router.register(r'ia', views.IAGenerationViewSet, basename='ia-generation')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération NFT, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
