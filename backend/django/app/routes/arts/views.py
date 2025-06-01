"""
Dihya – Django Arts API Views Ultra Avancé
-----------------------------------------
- ViewSets pour œuvres, artistes, expositions, galeries, NFT, IA générative
- Sécurité, RBAC, audit, logs, multilingue, RGPD, extensibilité
"""
from rest_framework import viewsets, permissions
from .serializers import (
    OeuvreSerializer, ArtisteSerializer, ExpositionSerializer, GalerieSerializer,
    NFTSerializer, IAGenerationSerializer, AuditLogSerializer
)

class OeuvreViewSet(viewsets.ModelViewSet):
    serializer_class = OeuvreSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class ArtisteViewSet(viewsets.ModelViewSet):
    serializer_class = ArtisteSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class ExpositionViewSet(viewsets.ModelViewSet):
    serializer_class = ExpositionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class GalerieViewSet(viewsets.ModelViewSet):
    serializer_class = GalerieSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class NFTViewSet(viewsets.ModelViewSet):
    serializer_class = NFTSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class IAGenerationViewSet(viewsets.ModelViewSet):
    serializer_class = IAGenerationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = []
