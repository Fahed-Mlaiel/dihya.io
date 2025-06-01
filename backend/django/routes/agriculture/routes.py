"""
Routes Django REST & GraphQL pour la gestion des projets agricoles.
Inclut sécurité, multilingue, audit, plugins, RGPD, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgricultureProjectViewSet

router = DefaultRouter()
router.register(r'agriculture-projects', AgricultureProjectViewSet, basename='agricultureproject')

urlpatterns = [
    path('', include(router.urls)),
]
# Pour GraphQL, voir intégration dans le schéma global du projet.
