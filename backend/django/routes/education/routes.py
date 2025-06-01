"""
Routes RESTful et GraphQL pour la gestion de projets éducatifs (écoles, formations, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('education/', views.EducationListView.as_view(), name='education-list'),
    path('education/<int:pk>/', views.EducationDetailView.as_view(), name='education-detail'),
    path('education/export/', views.EducationExportView.as_view(), name='education-export'),
    path('education/plugins/', views.EducationPluginListView.as_view(), name='education-plugins'),
    path('education/ia/', views.EducationIAView.as_view(), name='education-ia'),
]

# GraphQL schema intégré dans le module views
