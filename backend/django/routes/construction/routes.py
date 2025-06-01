"""
Routes RESTful et GraphQL pour la gestion de projets de construction (génie civil, architecture, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('construction/', views.ConstructionListView.as_view(), name='construction-list'),
    path('construction/<int:pk>/', views.ConstructionDetailView.as_view(), name='construction-detail'),
    path('construction/export/', views.ConstructionExportView.as_view(), name='construction-export'),
    path('construction/plugins/', views.ConstructionPluginListView.as_view(), name='construction-plugins'),
    path('construction/ia/', views.ConstructionIAView.as_view(), name='construction-ia'),
]

# GraphQL schema intégré dans le module views
