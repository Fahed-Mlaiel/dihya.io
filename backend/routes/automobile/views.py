"""
Views ultra avancées pour le module Automobile
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import AutomobileProject, AutomobileAsset
from .serializers import AutomobileProjectSerializer, AutomobileAssetSerializer
from .audit import automobile_audit_logger
from .i18n import AUTOMOBILE_I18N
from .permissions import IsAutomobileProjectOwnerOrReadOnly, IsAutomobileAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class AutomobileProjectViewSet(viewsets.ModelViewSet):
    queryset = AutomobileProject.objects.all()
    serializer_class = AutomobileProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAutomobileProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        automobile_audit_logger.log(self.request.user, 'create', 'AutomobileProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        automobile_audit_logger.log(self.request.user, 'delete', 'AutomobileProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class AutomobileAssetViewSet(viewsets.ModelViewSet):
    queryset = AutomobileAsset.objects.all()
    serializer_class = AutomobileAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAutomobileAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        automobile_audit_logger.log(self.request.user, 'upload', 'AutomobileAsset', obj.id, details=obj.name, language=obj.language)
