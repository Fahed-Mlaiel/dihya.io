"""
Dihya – Django Gamer API Routes Ultra Avancé
--------------------------------------------
- Endpoints REST pour profils, jeux, scores, classements, tournois, succès, inventaires, IA gaming, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST gamer (sécurité, multilingue, souveraineté)
🇬🇧 Django REST gamer routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للألعاب (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n gamer (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'profils', views.ProfilViewSet, basename='profil')
router.register(r'jeux', views.JeuViewSet, basename='jeu')
router.register(r'scores', views.ScoreViewSet, basename='score')
router.register(r'classements', views.ClassementViewSet, basename='classement')
router.register(r'tournois', views.TournoiViewSet, basename='tournoi')
router.register(r'succes', views.SuccesViewSet, basename='succes')
router.register(r'inventaires', views.InventaireViewSet, basename='inventaire')
router.register(r'ia', views.IAGamingViewSet, basename='ia-gaming')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
