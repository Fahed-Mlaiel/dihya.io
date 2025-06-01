"""
Routes RESTful et GraphQL pour la gestion de projets santé (hôpitaux, cliniques, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.HealthListView.as_view(), name='health-list'),
    path('health/<int:pk>/', views.HealthDetailView.as_view(), name='health-detail'),
    path('health/export/', views.HealthExportView.as_view(), name='health-export'),
    path('health/plugins/', views.HealthPluginListView.as_view(), name='health-plugins'),
    path('health/ia/', views.HealthIAView.as_view(), name='health-ia'),
]

# GraphQL schema intégré dans le module views
