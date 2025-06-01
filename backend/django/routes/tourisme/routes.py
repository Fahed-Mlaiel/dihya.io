"""
Routes RESTful et GraphQL pour la gestion de projets touristiques (voyages, hébergements, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('tourisme/', views.TourismeListView.as_view(), name='tourisme-list'),
    path('tourisme/<int:pk>/', views.TourismeDetailView.as_view(), name='tourisme-detail'),
    path('tourisme/export/', views.TourismeExportView.as_view(), name='tourisme-export'),
    path('tourisme/plugins/', views.TourismePluginListView.as_view(), name='tourisme-plugins'),
    path('tourisme/ia/', views.TourismeIAView.as_view(), name='tourisme-ia'),
]

# GraphQL schema intégré dans le module views
