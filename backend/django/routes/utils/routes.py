"""
Routes RESTful et GraphQL pour les utilitaires métiers (outils, scripts, automatisations, plugins, IA fallback).
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('utils/', views.UtilsListView.as_view(), name='utils-list'),
    path('utils/<int:pk>/', views.UtilsDetailView.as_view(), name='utils-detail'),
    path('utils/export/', views.UtilsExportView.as_view(), name='utils-export'),
    path('utils/plugins/', views.UtilsPluginListView.as_view(), name='utils-plugins'),
    path('utils/ia/', views.UtilsIAView.as_view(), name='utils-ia'),
]

# GraphQL schema intégré dans le module views
