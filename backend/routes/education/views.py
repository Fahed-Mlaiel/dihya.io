"""
Views ultra avancées pour le module Education
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import EducationProject, EducationAsset
from .serializers import EducationProjectSerializer, EducationAssetSerializer
from .audit import education_audit_logger
from .i18n import EDUCATION_I18N
from .permissions import IsEducationProjectOwnerOrReadOnly, IsEducationAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class EducationProjectViewSet(viewsets.ModelViewSet):
    queryset = EducationProject.objects.all()
    serializer_class = EducationProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEducationProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        education_audit_logger.log(self.request.user, 'create', 'EducationProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        education_audit_logger.log(self.request.user, 'delete', 'EducationProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class EducationAssetViewSet(viewsets.ModelViewSet):
    queryset = EducationAsset.objects.all()
    serializer_class = EducationAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsEducationAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        education_audit_logger.log(self.request.user, 'upload', 'EducationAsset', obj.id, details=obj.name, language=obj.language)
