"""
Routes RESTful et GraphQL pour la gestion de projets blockchain (crypto, NFT, smart contracts, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('blockchain/', views.BlockchainListView.as_view(), name='blockchain-list'),
    path('blockchain/<int:pk>/', views.BlockchainDetailView.as_view(), name='blockchain-detail'),
    path('blockchain/export/', views.BlockchainExportView.as_view(), name='blockchain-export'),
    path('blockchain/plugins/', views.BlockchainPluginListView.as_view(), name='blockchain-plugins'),
    path('blockchain/ia/', views.BlockchainIAView.as_view(), name='blockchain-ia'),
]

# GraphQL schema intégré dans le module views
