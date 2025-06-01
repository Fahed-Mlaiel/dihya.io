"""
Routes RESTful et GraphQL pour la gestion de projets gaming (jeux vidéo, e-sport, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('gamer/', views.GamerListView.as_view(), name='gamer-list'),
    path('gamer/<int:pk>/', views.GamerDetailView.as_view(), name='gamer-detail'),
    path('gamer/export/', views.GamerExportView.as_view(), name='gamer-export'),
    path('gamer/plugins/', views.GamerPluginListView.as_view(), name='gamer-plugins'),
    path('gamer/ia/', views.GamerIAView.as_view(), name='gamer-ia'),
]

# GraphQL schema intégré dans le module views
