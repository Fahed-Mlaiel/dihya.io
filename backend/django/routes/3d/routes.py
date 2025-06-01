"""
Routes RESTful et GraphQL pour la gestion de projets 3D (VR/AR, modélisation, etc.)
Sécurité maximale, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('3d/', views.Project3DListView.as_view(), name='3d-list'),
    path('3d/<int:pk>/', views.Project3DDetailView.as_view(), name='3d-detail'),
    path('3d/export/', views.Project3DExportView.as_view(), name='3d-export'),
    path('3d/plugins/', views.Project3DPluginListView.as_view(), name='3d-plugins'),
    path('3d/ia/', views.Project3DIAView.as_view(), name='3d-ia'),
]

# GraphQL schema intégré dans le module views
