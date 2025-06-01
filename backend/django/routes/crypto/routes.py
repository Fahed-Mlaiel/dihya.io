"""
Routes RESTful et GraphQL pour la gestion de projets crypto (échanges, wallets, DeFi, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('crypto/', views.CryptoListView.as_view(), name='crypto-list'),
    path('crypto/<int:pk>/', views.CryptoDetailView.as_view(), name='crypto-detail'),
    path('crypto/export/', views.CryptoExportView.as_view(), name='crypto-export'),
    path('crypto/plugins/', views.CryptoPluginListView.as_view(), name='crypto-plugins'),
    path('crypto/ia/', views.CryptoIAView.as_view(), name='crypto-ia'),
]

# GraphQL schema intégré dans le module views
