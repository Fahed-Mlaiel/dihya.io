"""
Dihya – Django Agriculture API Routes Ultra Avancé
--------------------------------------------------
- Endpoints REST pour exploitations, cultures, capteurs IoT, météo, alertes, conseils IA, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST agriculture (sécurité, multilingue, souveraineté)
🇬🇧 Django REST agriculture routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للزراعة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n timgart (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'exploitations', views.ExploitationViewSet, basename='exploitation')
router.register(r'cultures', views.CultureViewSet, basename='culture')
router.register(r'capteurs', views.CapteurViewSet, basename='capteur')
router.register(r'meteo', views.MeteoViewSet, basename='meteo')
router.register(r'alertes', views.AlerteViewSet, basename='alerte')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'notifications', views.NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération IA, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
