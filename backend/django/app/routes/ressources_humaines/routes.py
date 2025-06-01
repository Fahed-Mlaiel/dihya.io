"""
Dihya – Django Ressources Humaines API Routes Ultra Avancé
----------------------------------------------------------
- Endpoints REST pour employés, contrats, absences, congés, paie, recrutement, évaluations, formations, IA RH, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST RH (sécurité, multilingue, souveraineté)
🇬🇧 Django REST HR routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للموارد البشرية (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n imdanen (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'employes', views.EmployeViewSet, basename='employe')
router.register(r'contrats', views.ContratViewSet, basename='contrat')
router.register(r'absences', views.AbsenceViewSet, basename='absence')
router.register(r'conges', views.CongeViewSet, basename='conge')
router.register(r'paie', views.PaieViewSet, basename='paie')
router.register(r'recrutement', views.RecrutementViewSet, basename='recrutement')
router.register(r'evaluations', views.EvaluationViewSet, basename='evaluation')
router.register(r'formations', views.FormationViewSet, basename='formation')
router.register(r'ia', views.IARHViewSet, basename='ia-rh')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
