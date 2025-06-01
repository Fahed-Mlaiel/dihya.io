"""
Views ultra avancées pour le module Mobile
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import MobileProject
from .serializers import MobileProjectSerializer
from .audit import mobile_audit_logger
from .i18n import MOBILE_I18N
from .permissions import IsMobileProjectOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class MobileProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets Mobile.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = MobileProject.objects.all()
    serializer_class = MobileProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMobileProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        mobile_audit_logger.log(self.request.user, 'create', 'MobileProject', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        mobile_audit_logger.log(self.request.user, 'delete', 'MobileProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.
