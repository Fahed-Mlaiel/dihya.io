"""
Routes RESTful et GraphQL pour la gestion des validations métiers (audit, conformité, RGPD, plugins, IA fallback).
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('validators/', views.ValidatorListView.as_view(), name='validator-list'),
    path('validators/<int:pk>/', views.ValidatorDetailView.as_view(), name='validator-detail'),
    path('validators/export/', views.ValidatorExportView.as_view(), name='validator-export'),
    path('validators/plugins/', views.ValidatorPluginListView.as_view(), name='validator-plugins'),
    path('validators/ia/', views.ValidatorIAView.as_view(), name='validator-ia'),
]

# GraphQL schema intégré dans le module views
