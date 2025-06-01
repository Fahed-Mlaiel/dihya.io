"""
Dihya – Django Science API Routes Ultra Avancé
----------------------------------------------
- Endpoints REST pour publications, projets, expériences, jeux de données, lab notebooks, chercheurs, institutions, IA science, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, traçabilité scientifique, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST science (sécurité, multilingue, souveraineté)
🇬🇧 Django REST science routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للعلوم (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tamedyazt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'publications', views.PublicationViewSet, basename='publication')
router.register(r'projets', views.ProjetViewSet, basename='projet')
router.register(r'experiences', views.ExperienceViewSet, basename='experience')
router.register(r'jeux_donnees', views.JeuDonneesViewSet, basename='jeu-donnees')
router.register(r'lab_notebooks', views.LabNotebookViewSet, basename='lab-notebook')
router.register(r'chercheurs', views.ChercheurViewSet, basename='chercheur')
router.register(r'institutions', views.InstitutionViewSet, basename='institution')
router.register(r'ia', views.IAScienceViewSet, basename='ia-science')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, traçabilité scientifique, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
