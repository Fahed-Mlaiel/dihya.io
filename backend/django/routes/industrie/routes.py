"""
Routes RESTful et GraphQL pour la gestion de projets industriels (usines, supply chain, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('industrie/', views.IndustrieListView.as_view(), name='industrie-list'),
    path('industrie/<int:pk>/', views.IndustrieDetailView.as_view(), name='industrie-detail'),
    path('industrie/export/', views.IndustrieExportView.as_view(), name='industrie-export'),
    path('industrie/plugins/', views.IndustriePluginListView.as_view(), name='industrie-plugins'),
    path('industrie/ia/', views.IndustrieIAView.as_view(), name='industrie-ia'),
]

# GraphQL schema intégré dans le module views
