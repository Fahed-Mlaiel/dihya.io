"""
Routes RESTful et GraphQL pour la gestion de projets de journalisme (médias, presse, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('journalisme/', views.JournalismeListView.as_view(), name='journalisme-list'),
    path('journalisme/<int:pk>/', views.JournalismeDetailView.as_view(), name='journalisme-detail'),
    path('journalisme/export/', views.JournalismeExportView.as_view(), name='journalisme-export'),
    path('journalisme/plugins/', views.JournalismePluginListView.as_view(), name='journalisme-plugins'),
    path('journalisme/ia/', views.JournalismeIAView.as_view(), name='journalisme-ia'),
]

# GraphQL schema intégré dans le module views
