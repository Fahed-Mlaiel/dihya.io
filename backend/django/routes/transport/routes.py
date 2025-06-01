"""
Routes RESTful et GraphQL pour la gestion de projets de transport (logistique, mobilité, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('transport/', views.TransportListView.as_view(), name='transport-list'),
    path('transport/<int:pk>/', views.TransportDetailView.as_view(), name='transport-detail'),
    path('transport/export/', views.TransportExportView.as_view(), name='transport-export'),
    path('transport/plugins/', views.TransportPluginListView.as_view(), name='transport-plugins'),
    path('transport/ia/', views.TransportIAView.as_view(), name='transport-ia'),
]

# GraphQL schema intégré dans le module views
