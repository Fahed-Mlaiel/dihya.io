"""
Dihya – Django Éducation API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour établissements, classes, enseignants, élèves, cours, examens, notes, certifications, IA pédagogique, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST éducation (sécurité, multilingue, souveraineté)
🇬🇧 Django REST education routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للتعليم (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tamedyazt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'etablissements', views.EtablissementViewSet, basename='etablissement')
router.register(r'classes', views.ClasseViewSet, basename='classe')
router.register(r'enseignants', views.EnseignantViewSet, basename='enseignant')
router.register(r'eleves', views.EleveViewSet, basename='eleve')
router.register(r'cours', views.CoursViewSet, basename='cours')
router.register(r'examens', views.ExamenViewSet, basename='examen')
router.register(r'notes', views.NoteViewSet, basename='note')
router.register(r'certifications', views.CertificationViewSet, basename='certification')
router.register(r'ia', views.IAPedagogiqueViewSet, basename='ia-pedagogique')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
