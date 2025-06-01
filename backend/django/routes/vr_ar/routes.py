"""
Routes Django REST & GraphQL pour la gestion des projets VR/AR.
Inclut sécurité, multilingue, audit, plugins, RGPD, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VRARProjectViewSet

router = DefaultRouter()
router.register(r'vrar-projects', VRARProjectViewSet, basename='vrarproject')

urlpatterns = [
    path('', include(router.urls)),
]
# Pour GraphQL, voir intégration dans le schéma global du projet.
