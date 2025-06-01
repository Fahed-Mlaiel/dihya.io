"""
Routes RESTful et GraphQL pour la gestion de projets immobiliers (agences, gestion locative, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('immobilier/', views.ImmobilierListView.as_view(), name='immobilier-list'),
    path('immobilier/<int:pk>/', views.ImmobilierDetailView.as_view(), name='immobilier-detail'),
    path('immobilier/export/', views.ImmobilierExportView.as_view(), name='immobilier-export'),
    path('immobilier/plugins/', views.ImmobilierPluginListView.as_view(), name='immobilier-plugins'),
    path('immobilier/ia/', views.ImmobilierIAView.as_view(), name='immobilier-ia'),
]

# GraphQL schema intégré dans le module views
