"""
Routes RESTful et GraphQL pour la gestion de projets IT/DevOps (cloud, CI/CD, monitoring, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('it-devops/', views.ITDevOpsListView.as_view(), name='it-devops-list'),
    path('it-devops/<int:pk>/', views.ITDevOpsDetailView.as_view(), name='it-devops-detail'),
    path('it-devops/export/', views.ITDevOpsExportView.as_view(), name='it-devops-export'),
    path('it-devops/plugins/', views.ITDevOpsPluginListView.as_view(), name='it-devops-plugins'),
    path('it-devops/ia/', views.ITDevOpsIAView.as_view(), name='it-devops-ia'),
]

# GraphQL schema intégré dans le module views
