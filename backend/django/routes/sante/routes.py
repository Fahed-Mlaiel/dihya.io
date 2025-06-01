"""
Dihya – Django Santé API Routes Ultra Avancé
-------------------------------------------
- Endpoints REST pour patients, dossiers, rendez-vous, prescriptions, logs, audit, IA, plugins
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST Santé (sécurité, multilingue, souveraineté)
🇬🇧 Django REST Health routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للصحة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n Santé (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet, basename='patient')
router.register(r'dossiers', views.DossierViewSet, basename='dossier')
router.register(r'rendezvous', views.RendezVousViewSet, basename='rendezvous')
router.register(r'prescriptions', views.PrescriptionViewSet, basename='prescription')
router.register(r'ia', views.IASanteViewSet, basename='ia-sante')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
