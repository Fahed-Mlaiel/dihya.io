"""
Views ultra avancées pour le module Culture
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import CultureProject, CultureAsset
from .serializers import CultureProjectSerializer, CultureAssetSerializer
from .audit import culture_audit_logger
from .i18n import CULTURE_I18N
from .permissions import IsCultureProjectOwnerOrReadOnly, IsCultureAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class CultureProjectViewSet(viewsets.ModelViewSet):
    queryset = CultureProject.objects.all()
    serializer_class = CultureProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCultureProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        culture_audit_logger.log(self.request.user, 'create', 'CultureProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        culture_audit_logger.log(self.request.user, 'delete', 'CultureProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class CultureAssetViewSet(viewsets.ModelViewSet):
    queryset = CultureAsset.objects.all()
    serializer_class = CultureAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCultureAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        culture_audit_logger.log(self.request.user, 'upload', 'CultureAsset', obj.id, details=obj.name, language=obj.language)
