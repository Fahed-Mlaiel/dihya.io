"""
Routes Django REST & GraphQL pour la gestion des projets artistiques.
Inclut sécurité, multilingue, audit, plugins, RGPD, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtProjectViewSet

router = DefaultRouter()
router.register(r'art-projects', ArtProjectViewSet, basename='artproject')

urlpatterns = [
    path('', include(router.urls)),
]
# Pour GraphQL, voir intégration dans le schéma global du projet.
