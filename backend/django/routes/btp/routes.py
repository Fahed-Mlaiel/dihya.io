"""
Routes RESTful et GraphQL pour la gestion de projets BTP (bâtiment, travaux publics, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('btp/', views.BTPListView.as_view(), name='btp-list'),
    path('btp/<int:pk>/', views.BTPDetailView.as_view(), name='btp-detail'),
    path('btp/export/', views.BTPExportView.as_view(), name='btp-export'),
    path('btp/plugins/', views.BTPPluginListView.as_view(), name='btp-plugins'),
    path('btp/ia/', views.BTPIAView.as_view(), name='btp-ia'),
]

# GraphQL schema intégré dans le module views
