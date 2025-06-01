"""
Dihya – Vues Django REST pour le module Sécurité
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import IncidentSecurite, AlerteSecurite, ControleSecurite
from .serializers import IncidentSecuriteSerializer, AlerteSecuriteSerializer, ControleSecuriteSerializer
from .permissions import IsSecuriteAdminOrReadOnly

class IncidentSecuriteViewSet(viewsets.ModelViewSet):
    queryset = IncidentSecurite.objects.all()
    serializer_class = IncidentSecuriteSerializer
    permission_classes = [IsSecuriteAdminOrReadOnly]

class AlerteSecuriteViewSet(viewsets.ModelViewSet):
    queryset = AlerteSecurite.objects.all()
    serializer_class = AlerteSecuriteSerializer
    permission_classes = [IsSecuriteAdminOrReadOnly]

class ControleSecuriteViewSet(viewsets.ModelViewSet):
    queryset = ControleSecurite.objects.all()
    serializer_class = ControleSecuriteSerializer
    permission_classes = [IsSecuriteAdminOrReadOnly]
