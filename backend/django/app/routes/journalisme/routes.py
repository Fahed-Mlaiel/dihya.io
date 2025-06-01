"""
Dihya – Django Journalisme API Routes Ultra Avancé
--------------------------------------------------
- Endpoints REST pour articles, journalistes, rubriques, médias, commentaires, publications, IA rédactionnelle, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST journalisme (sécurité, multilingue, souveraineté)
🇬🇧 Django REST journalism routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للصحافة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n ajurnalism (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet, basename='article')
router.register(r'journalistes', views.JournalisteViewSet, basename='journaliste')
router.register(r'rubriques', views.RubriqueViewSet, basename='rubrique')
router.register(r'medias', views.MediaViewSet, basename='media')
router.register(r'commentaires', views.CommentaireViewSet, basename='commentaire')
router.register(r'publications', views.PublicationViewSet, basename='publication')
router.register(r'ia', views.IARedactionnelleViewSet, basename='ia-redactionnelle')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
