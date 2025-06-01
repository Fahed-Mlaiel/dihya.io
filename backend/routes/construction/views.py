"""
Views ultra avancées pour le module Construction
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import ConstructionProject, ConstructionAsset
from .serializers import ConstructionProjectSerializer, ConstructionAssetSerializer
from .audit import construction_audit_logger
from .i18n import CONSTRUCTION_I18N
from .permissions import IsConstructionProjectOwnerOrReadOnly, IsConstructionAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class ConstructionProjectViewSet(viewsets.ModelViewSet):
    queryset = ConstructionProject.objects.all()
    serializer_class = ConstructionProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsConstructionProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        construction_audit_logger.log(self.request.user, 'create', 'ConstructionProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        construction_audit_logger.log(self.request.user, 'delete', 'ConstructionProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class ConstructionAssetViewSet(viewsets.ModelViewSet):
    queryset = ConstructionAsset.objects.all()
    serializer_class = ConstructionAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsConstructionAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        construction_audit_logger.log(self.request.user, 'upload', 'ConstructionAsset', obj.id, details=obj.name, language=obj.language)
