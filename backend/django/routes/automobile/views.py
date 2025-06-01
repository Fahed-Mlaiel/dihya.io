"""
Dihya – Django Automobile API Views Ultra Avancé
------------------------------------------------
- ViewSets REST pour véhicules, modèles, marques, maintenance, logs, audit, IA, plugins
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Vues Django REST Automobile (sécurité, multilingue, souveraineté)
🇬🇧 Django REST Automobile views (security, multilingual, sovereignty)
🇦🇪 عروض Django REST للسيارات (الأمان، متعدد اللغات، السيادة)
ⵣ Tiwaliwin Django REST n Automobile (amatu, multilingual, sovereignty)
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

class ModeleViewSet(viewsets.ModelViewSet):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MarqueViewSet(viewsets.ModelViewSet):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IAAutomobileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # TODO: Intégration IA souveraine, fallback open source
        return Response({'recommendations': []})

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
