"""
Dihya – Django Health API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour patients, dossiers médicaux, rendez-vous, praticiens, prescriptions, analyses, IA santé, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST santé (sécurité, multilingue, souveraineté)
🇬🇧 Django REST health routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للصحة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tafuyt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet, basename='patient')
router.register(r'dossiers', views.DossierMedicalViewSet, basename='dossier-medical')
router.register(r'rendezvous', views.RendezVousViewSet, basename='rendezvous')
router.register(r'praticiens', views.PraticienViewSet, basename='praticien')
router.register(r'prescriptions', views.PrescriptionViewSet, basename='prescription')
router.register(r'analyses', views.AnalyseViewSet, basename='analyse')
router.register(r'ia', views.IASanteViewSet, basename='ia-sante')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
