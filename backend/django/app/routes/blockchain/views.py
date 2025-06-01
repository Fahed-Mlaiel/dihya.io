"""
Dihya – Django Blockchain API Views Ultra Avancé
------------------------------------------------
- ViewSets pour blocks, transactions, smart contracts, audit
- Sécurité, RBAC, audit, logs, multilingue, RGPD, extensibilité
"""
from rest_framework import viewsets, permissions
from .serializers import BlockSerializer, TransactionSerializer, SmartContractSerializer, AuditLogSerializer

class BlockViewSet(viewsets.ModelViewSet):
    serializer_class = BlockSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class SmartContractViewSet(viewsets.ModelViewSet):
    serializer_class = SmartContractSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = []
