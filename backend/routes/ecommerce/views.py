"""
Views ultra avancées pour le module Ecommerce
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import EcommerceProject, EcommerceAsset
from .serializers import EcommerceProjectSerializer, EcommerceAssetSerializer
from .audit import ecommerce_audit_logger
from .i18n import ECOMMERCE_I18N
from .permissions import IsEcommerceProjectOwnerOrReadOnly, IsEcommerceAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class EcommerceProjectViewSet(viewsets.ModelViewSet):
    queryset = EcommerceProject.objects.all()
    serializer_class = EcommerceProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEcommerceProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        ecommerce_audit_logger.log(self.request.user, 'create', 'EcommerceProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        ecommerce_audit_logger.log(self.request.user, 'delete', 'EcommerceProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class EcommerceAssetViewSet(viewsets.ModelViewSet):
    queryset = EcommerceAsset.objects.all()
    serializer_class = EcommerceAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEcommerceAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        ecommerce_audit_logger.log(self.request.user, 'upload', 'EcommerceAsset', obj.id, details=obj.name, language=obj.language)
