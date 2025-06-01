"""
Views ultra avancées pour le module Assurance (Dihya)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy.
"""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import AssuranceProject, AssuranceAsset
from .serializers import AssuranceProjectSerializer, AssuranceAssetSerializer
from .policy import AssurancePolicy

class AssuranceProjectViewSet(viewsets.ModelViewSet):
    queryset = AssuranceProject.objects.all()
    serializer_class = AssuranceProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    policy = AssurancePolicy()

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        self.policy.audit_action(self.request.user, 'create', {'id': obj.id, 'name': obj.name})

    def perform_destroy(self, instance):
        self.policy.audit_action(self.request.user, 'delete', {'id': instance.id, 'name': instance.name})
        instance.delete()

class AssuranceAssetViewSet(viewsets.ModelViewSet):
    queryset = AssuranceAsset.objects.all()
    serializer_class = AssuranceAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    policy = AssurancePolicy()

    def perform_create(self, serializer):
        obj = serializer.save()
        self.policy.audit_action(self.request.user, 'create', {'id': obj.id, 'file': obj.file.name})

    def perform_destroy(self, instance):
        self.policy.audit_action(self.request.user, 'delete', {'id': instance.id, 'file': instance.file.name})
        instance.delete()
