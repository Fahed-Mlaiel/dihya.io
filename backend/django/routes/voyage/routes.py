"""
Routes RESTful et GraphQL pour la gestion de projets de voyage (réservations, itinéraires, IA, plugins, audit, RGPD, SEO).
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('voyage/', views.VoyageListView.as_view(), name='voyage-list'),
    path('voyage/<int:pk>/', views.VoyageDetailView.as_view(), name='voyage-detail'),
    path('voyage/export/', views.VoyageExportView.as_view(), name='voyage-export'),
    path('voyage/plugins/', views.VoyagePluginListView.as_view(), name='voyage-plugins'),
    path('voyage/ia/', views.VoyageIAView.as_view(), name='voyage-ia'),
]

# GraphQL schema intégré dans le module views
