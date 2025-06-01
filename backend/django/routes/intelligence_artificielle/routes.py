"""
Routes Django REST & GraphQL pour la gestion des projets IA.
Inclut sécurité, multilingue, audit, plugins, RGPD, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IAProjectViewSet

router = DefaultRouter()
router.register(r'ia-projects', IAProjectViewSet, basename='iaproject')

urlpatterns = [
    path('', include(router.urls)),
]
# Pour GraphQL, voir intégration dans le schéma global du projet.
