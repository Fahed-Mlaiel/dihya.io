"""
Routes RESTful et GraphQL pour la gestion de projets e-commerce (boutiques, marketplaces, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('ecommerce/', views.EcommerceListView.as_view(), name='ecommerce-list'),
    path('ecommerce/<int:pk>/', views.EcommerceDetailView.as_view(), name='ecommerce-detail'),
    path('ecommerce/export/', views.EcommerceExportView.as_view(), name='ecommerce-export'),
    path('ecommerce/plugins/', views.EcommercePluginListView.as_view(), name='ecommerce-plugins'),
    path('ecommerce/ia/', views.EcommerceIAView.as_view(), name='ecommerce-ia'),
]

# GraphQL schema intégré dans le module views
