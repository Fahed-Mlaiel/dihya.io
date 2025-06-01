"""
Dihya – Django Agriculture API Views Ultra Avancé
------------------------------------------------
- ViewSets pour exploitations, cultures, capteurs IoT, météo, alertes, conseils IA
- Sécurité, RBAC, audit, logs, multilingue, RGPD, extensibilité
"""
from rest_framework import viewsets, permissions
from .serializers import (
    ExploitationSerializer, CultureSerializer, CapteurSerializer, MeteoSerializer,
    AlerteSerializer, RapportSerializer, NotificationSerializer
)

class ExploitationViewSet(viewsets.ModelViewSet):
    serializer_class = ExploitationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []  # À remplacer par la vraie source de données

class CultureViewSet(viewsets.ModelViewSet):
    serializer_class = CultureSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class CapteurViewSet(viewsets.ModelViewSet):
    serializer_class = CapteurSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class MeteoViewSet(viewsets.ModelViewSet):
    serializer_class = MeteoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class AlerteViewSet(viewsets.ModelViewSet):
    serializer_class = AlerteSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class RapportViewSet(viewsets.ModelViewSet):
    serializer_class = RapportSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []
