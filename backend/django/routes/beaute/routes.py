"""
Routes RESTful et GraphQL pour la gestion de projets beauté (cosmétique, bien-être, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('beaute/', views.BeauteListView.as_view(), name='beaute-list'),
    path('beaute/<int:pk>/', views.BeauteDetailView.as_view(), name='beaute-detail'),
    path('beaute/export/', views.BeauteExportView.as_view(), name='beaute-export'),
    path('beaute/plugins/', views.BeautePluginListView.as_view(), name='beaute-plugins'),
    path('beaute/ia/', views.BeauteIAView.as_view(), name='beaute-ia'),
]

# GraphQL schema intégré dans le module views
