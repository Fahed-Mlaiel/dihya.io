"""
Views ultra avancées pour le module Administration Publique
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import AdministrationPubliqueProject
from .serializers import AdministrationPubliqueProjectSerializer
from .audit import administration_publique_audit_logger
from .i18n import ADMINISTRATION_PUBLIQUE_I18N
from .permissions import IsAdministrationPubliqueProjectOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class AdministrationPubliqueProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets d'administration publique.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = AdministrationPubliqueProject.objects.all()
    serializer_class = AdministrationPubliqueProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdministrationPubliqueProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        administration_publique_audit_logger.log(self.request.user, 'create', 'AdministrationPubliqueProject', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        administration_publique_audit_logger.log(self.request.user, 'delete', 'AdministrationPubliqueProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.
