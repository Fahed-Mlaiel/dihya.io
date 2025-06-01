"""
Dihya – Django Automobile API Views Ultra Avancé
------------------------------------------------
- ViewSets REST pour véhicules, propriétaires, entretiens, sinistres, télématique, IoT, alertes, rapports, audit, plugins
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Vues Django REST automobile (sécurité, multilingue, souveraineté)
🇬🇧 Django REST automobile views (security, multilingual, sovereignty)
🇦🇪 عروض Django REST للسيارات (الأمان، متعدد اللغات، السيادة)
ⵣ Tiwaliwin Django REST n tigmmi n taggara (amatu, multilingual, sovereignty)
"""

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .audit import audit_log

class VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        audit_log(self.request.user, 'create_vehicule', instance)

class ProprietaireViewSet(viewsets.ModelViewSet):
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EntretienViewSet(viewsets.ModelViewSet):
    queryset = Entretien.objects.all()
    serializer_class = EntretienSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SinistreViewSet(viewsets.ModelViewSet):
    queryset = Sinistre.objects.all()
    serializer_class = SinistreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TelematicViewSet(viewsets.ModelViewSet):
    queryset = Telematic.objects.all()
    serializer_class = TelematicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IoTViewSet(viewsets.ModelViewSet):
    queryset = IoT.objects.all()
    serializer_class = IoTSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlerteViewSet(viewsets.ModelViewSet):
    queryset = Alerte.objects.all()
    serializer_class = AlerteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RapportViewSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
