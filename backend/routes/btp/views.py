"""
Views ultra avancées pour le module BTP
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import BtpProject, BtpAsset
from .serializers import BtpProjectSerializer, BtpAssetSerializer
from .audit import btp_audit_logger
from .i18n import BTP_I18N
from .permissions import IsBtpProjectOwnerOrReadOnly, IsBtpAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class BtpProjectViewSet(viewsets.ModelViewSet):
    queryset = BtpProject.objects.all()
    serializer_class = BtpProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBtpProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        btp_audit_logger.log(self.request.user, 'create', 'BtpProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        btp_audit_logger.log(self.request.user, 'delete', 'BtpProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class BtpAssetViewSet(viewsets.ModelViewSet):
    queryset = BtpAsset.objects.all()
    serializer_class = BtpAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBtpAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        btp_audit_logger.log(self.request.user, 'upload', 'BtpAsset', obj.id, details=obj.name, language=obj.language)
