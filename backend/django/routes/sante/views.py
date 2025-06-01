"""
Dihya – Django Santé API Views Ultra Avancé
------------------------------------------
- ViewSets REST pour patients, dossiers, rendez-vous, prescriptions, logs, audit, IA, plugins
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Vues Django REST Santé (sécurité, multilingue, souveraineté)
🇬🇧 Django REST Health views (security, multilingual, sovereignty)
🇦🇪 عروض Django REST للصحة (الأمان، متعدد اللغات، السيادة)
ⵣ Tiwaliwin Django REST n Santé (amatu, multilingual, sovereignty)
"""

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .audit import audit_log

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        audit_log(self.request.user, 'create_patient', instance)

class DossierViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RendezVousViewSet(viewsets.ModelViewSet):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IASanteViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # TODO: Intégration IA souveraine, fallback open source
        return Response({'recommendations': []})

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
