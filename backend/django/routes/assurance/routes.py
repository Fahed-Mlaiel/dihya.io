"""
Routes RESTful et GraphQL pour la gestion de projets d'assurance (santé, auto, habitation, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('assurance/', views.AssuranceListView.as_view(), name='assurance-list'),
    path('assurance/<int:pk>/', views.AssuranceDetailView.as_view(), name='assurance-detail'),
    path('assurance/export/', views.AssuranceExportView.as_view(), name='assurance-export'),
    path('assurance/plugins/', views.AssurancePluginListView.as_view(), name='assurance-plugins'),
    path('assurance/ia/', views.AssuranceIAView.as_view(), name='assurance-ia'),
]

# GraphQL schema intégré dans le module views
