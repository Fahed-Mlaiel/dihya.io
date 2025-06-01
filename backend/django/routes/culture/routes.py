"""
Routes RESTful et GraphQL pour la gestion de projets culturels (événements, patrimoine, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('culture/', views.CultureListView.as_view(), name='culture-list'),
    path('culture/<int:pk>/', views.CultureDetailView.as_view(), name='culture-detail'),
    path('culture/export/', views.CultureExportView.as_view(), name='culture-export'),
    path('culture/plugins/', views.CulturePluginListView.as_view(), name='culture-plugins'),
    path('culture/ia/', views.CultureIAView.as_view(), name='culture-ia'),
]

# GraphQL schema intégré dans le module views
