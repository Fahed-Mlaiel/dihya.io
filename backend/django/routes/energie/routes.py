"""
Routes RESTful et GraphQL pour la gestion de projets énergétiques (solaire, éolien, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('energie/', views.EnergieListView.as_view(), name='energie-list'),
    path('energie/<int:pk>/', views.EnergieDetailView.as_view(), name='energie-detail'),
    path('energie/export/', views.EnergieExportView.as_view(), name='energie-export'),
    path('energie/plugins/', views.EnergiePluginListView.as_view(), name='energie-plugins'),
    path('energie/ia/', views.EnergieIAView.as_view(), name='energie-ia'),
]

# GraphQL schema intégré dans le module views
