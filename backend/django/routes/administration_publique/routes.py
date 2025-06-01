"""
Routes Django REST & GraphQL pour la gestion des projets d'administration publique.
Inclut sécurité, multilingue, audit, plugins, RGPD, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdministrationPubliqueProjectViewSet

router = DefaultRouter()
router.register(r'administration-publique-projects', AdministrationPubliqueProjectViewSet, basename='administrationpubliqueproject')

urlpatterns = [
    path('', include(router.urls)),
]
# Pour GraphQL, voir intégration dans le schéma global du projet.
