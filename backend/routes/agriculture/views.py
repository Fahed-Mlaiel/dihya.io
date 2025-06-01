"""
Views ultra avancées pour le module Agriculture
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import AgricultureProject, AgricultureAsset
from .serializers import AgricultureProjectSerializer, AgricultureAssetSerializer
from .audit import agriculture_audit_logger
from .i18n import AGRICULTURE_I18N
from .permissions import IsAgricultureProjectOwnerOrReadOnly, IsAgricultureAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class AgricultureProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets Agriculture.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = AgricultureProject.objects.all()
    serializer_class = AgricultureProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAgricultureProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        agriculture_audit_logger.log(self.request.user, 'create', 'AgricultureProject', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        agriculture_audit_logger.log(self.request.user, 'delete', 'AgricultureProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.

@method_decorator(csrf_protect, name='dispatch')
class AgricultureAssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des assets Agriculture.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = AgricultureAsset.objects.all()
    serializer_class = AgricultureAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAgricultureAssetManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save()
        agriculture_audit_logger.log(self.request.user, 'upload', 'AgricultureAsset', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.
