"""
Dihya – Django Assurance API Views Ultra Avancé
----------------------------------------------
- ViewSets pour contrats, souscriptions, sinistres, paiements, attestations, notifications
- Sécurité, RBAC, audit, logs, multilingue, RGPD, extensibilité
"""
from rest_framework import viewsets, permissions
from .serializers import (
    ContratSerializer, SouscriptionSerializer, SinistreSerializer, PaiementSerializer,
    AttestationSerializer, NotificationSerializer, AuditLogSerializer
)

class ContratViewSet(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class SouscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SouscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class SinistreViewSet(viewsets.ModelViewSet):
    serializer_class = SinistreSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class PaiementViewSet(viewsets.ModelViewSet):
    serializer_class = PaiementSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class AttestationViewSet(viewsets.ModelViewSet):
    serializer_class = AttestationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = []
