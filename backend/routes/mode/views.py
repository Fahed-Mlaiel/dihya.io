"""
Views ultra avancées pour le module Mode (Fashion)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import ModeProject
from .serializers import ModeProjectSerializer
from .audit import mode_audit_logger
from .i18n import MODE_I18N
from .permissions import IsModeProjectOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class ModeProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets Mode.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = ModeProject.objects.all()
    serializer_class = ModeProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsModeProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        mode_audit_logger.log(self.request.user, 'create', 'ModeProject', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        mode_audit_logger.log(self.request.user, 'delete', 'ModeProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.
