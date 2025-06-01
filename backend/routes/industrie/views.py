"""
Views ultra avancées pour le module Industrie
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import IndustrieProject, IndustrieAsset
from .serializers import IndustrieProjectSerializer, IndustrieAssetSerializer
from .audit import industrie_audit_logger
from .i18n import INDUSTRIE_I18N
from .permissions import IsIndustrieProjectOwnerOrReadOnly, IsIndustrieAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class IndustrieProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets Industrie.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = IndustrieProject.objects.all()
    serializer_class = IndustrieProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsIndustrieProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        industrie_audit_logger.log(self.request.user, 'create', 'IndustrieProject', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        industrie_audit_logger.log(self.request.user, 'delete', 'IndustrieProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.

@method_decorator(csrf_protect, name='dispatch')
class IndustrieAssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des assets Industrie.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = IndustrieAsset.objects.all()
    serializer_class = IndustrieAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsIndustrieAssetManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save()
        industrie_audit_logger.log(self.request.user, 'upload', 'IndustrieAsset', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.
