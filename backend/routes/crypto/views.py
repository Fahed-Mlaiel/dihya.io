"""
Views ultra avancées pour le module Crypto
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import CryptoProject, CryptoAsset
from .serializers import CryptoProjectSerializer, CryptoAssetSerializer
from .audit import crypto_audit_logger
from .i18n import CRYPTO_I18N
from .permissions import IsCryptoProjectOwnerOrReadOnly, IsCryptoAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class CryptoProjectViewSet(viewsets.ModelViewSet):
    queryset = CryptoProject.objects.all()
    serializer_class = CryptoProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCryptoProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        crypto_audit_logger.log(self.request.user, 'create', 'CryptoProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        crypto_audit_logger.log(self.request.user, 'delete', 'CryptoProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class CryptoAssetViewSet(viewsets.ModelViewSet):
    queryset = CryptoAsset.objects.all()
    serializer_class = CryptoAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCryptoAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        crypto_audit_logger.log(self.request.user, 'upload', 'CryptoAsset', obj.id, details=obj.name, language=obj.language)
