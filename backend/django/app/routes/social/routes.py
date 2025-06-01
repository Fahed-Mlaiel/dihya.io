"""
Dihya – Django Social API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour profils, posts, commentaires, likes, partages, abonnements, notifications, IA social, modération, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, modération IA, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST social (sécurité, multilingue, souveraineté)
🇬🇧 Django REST social routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للتواصل الاجتماعي (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tamedyazt n tamedyazt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'profils', views.ProfilViewSet, basename='profil')
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'commentaires', views.CommentaireViewSet, basename='commentaire')
router.register(r'likes', views.LikeViewSet, basename='like')
router.register(r'partages', views.PartageViewSet, basename='partage')
router.register(r'abonnements', views.AbonnementViewSet, basename='abonnement')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'ia', views.IASocialViewSet, basename='ia-social')
router.register(r'moderation', views.ModerationViewSet, basename='moderation')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'logs', views.LogSocialViewSet, basename='log-social')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, modération IA, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
