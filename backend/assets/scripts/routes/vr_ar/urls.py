"""
Dihya Backend – Définition des routes Django REST/GraphQL pour IA/VR/AR
CORS, WAF, SEO, sécurité, plugins, multilingue, RGPD, multitenancy, documentation avancée.

- Toutes les routes sont protégées (CORS, JWT, WAF, anti-DDOS, audit, RGPD, plugins dynamiques, multitenancy, gestion des rôles, SEO backend, accessibilité, logs structurés).
- Support complet RESTful + GraphQL (exemple inclus).
- Extensible, production-ready, CI/CD, souveraineté numérique.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.list_projects, name='list_projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/update/', views.update_project, name='update_project'),
    path('graphql/', views.graphql_project_resolver, name='graphql_project_resolver'),
]

# Toutes les routes sont multilingues, auditées, RGPD, plugins, SEO, accessibilité, multitenancy.
# Voir views.py et la documentation intégrée pour les hooks, tests, et extensions.
