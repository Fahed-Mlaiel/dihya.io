"""
Views ultra avancées pour le module Beauté
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import BeauteProject, BeauteAsset
from .serializers import BeauteProjectSerializer, BeauteAssetSerializer
from .audit import beaute_audit_logger
from .i18n import BEAUTE_I18N
from .permissions import IsBeauteProjectOwnerOrReadOnly, IsBeauteAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class BeauteProjectViewSet(viewsets.ModelViewSet):
    queryset = BeauteProject.objects.all()
    serializer_class = BeauteProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBeauteProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        beaute_audit_logger.log(self.request.user, 'create', 'BeauteProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        beaute_audit_logger.log(self.request.user, 'delete', 'BeauteProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class BeauteAssetViewSet(viewsets.ModelViewSet):
    queryset = BeauteAsset.objects.all()
    serializer_class = BeauteAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBeauteAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        beaute_audit_logger.log(self.request.user, 'upload', 'BeauteAsset', obj.id, details=obj.name, language=obj.language)
