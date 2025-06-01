"""
Routes RESTful et GraphQL pour la gestion de projets hôtellerie (hôtels, restaurants, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('hotellerie/', views.HotellerieListView.as_view(), name='hotellerie-list'),
    path('hotellerie/<int:pk>/', views.HotellerieDetailView.as_view(), name='hotellerie-detail'),
    path('hotellerie/export/', views.HotellerieExportView.as_view(), name='hotellerie-export'),
    path('hotellerie/plugins/', views.HotelleriePluginListView.as_view(), name='hotellerie-plugins'),
    path('hotellerie/ia/', views.HotellerieIAView.as_view(), name='hotellerie-ia'),
]

# GraphQL schema intégré dans le module views
