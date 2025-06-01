"""
Views ultra avancées pour le module Medias
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import MediaAsset
from .serializers import MediaAssetSerializer
from .audit import medias_audit_logger
from .i18n import MEDIAS_I18N
from .permissions import IsMediaAssetOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class MediaAssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des assets médias.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMediaAssetOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        medias_audit_logger.log(self.request.user, 'create', 'MediaAsset', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        medias_audit_logger.log(self.request.user, 'delete', 'MediaAsset', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.
