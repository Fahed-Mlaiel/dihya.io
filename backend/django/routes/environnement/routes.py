"""
Routes RESTful et GraphQL pour la gestion de projets environnementaux (biodiversité, climat, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('environnement/', views.EnvironnementListView.as_view(), name='environnement-list'),
    path('environnement/<int:pk>/', views.EnvironnementDetailView.as_view(), name='environnement-detail'),
    path('environnement/export/', views.EnvironnementExportView.as_view(), name='environnement-export'),
    path('environnement/plugins/', views.EnvironnementPluginListView.as_view(), name='environnement-plugins'),
    path('environnement/ia/', views.EnvironnementIAView.as_view(), name='environnement-ia'),
]

# GraphQL schema intégré dans le module views
