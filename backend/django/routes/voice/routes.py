"""
Routes RESTful et GraphQL pour la gestion de la voix (synthèse, reconnaissance, bots, plugins, IA fallback).
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('voice/', views.VoiceListView.as_view(), name='voice-list'),
    path('voice/<int:pk>/', views.VoiceDetailView.as_view(), name='voice-detail'),
    path('voice/export/', views.VoiceExportView.as_view(), name='voice-export'),
    path('voice/plugins/', views.VoicePluginListView.as_view(), name='voice-plugins'),
    path('voice/ia/', views.VoiceIAView.as_view(), name='voice-ia'),
]

# GraphQL schema intégré dans le module views
