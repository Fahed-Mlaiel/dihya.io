"""
Routes Django REST & GraphQL pour la gestion des projets banque/finance.
Inclut sécurité, multilingue, audit, plugins, RGPD, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BanqueFinanceProjectViewSet

router = DefaultRouter()
router.register(r'banque-finance-projects', BanqueFinanceProjectViewSet, basename='banquefinanceproject')

urlpatterns = [
    path('', include(router.urls)),
]
# Pour GraphQL, voir intégration dans le schéma global du projet.
