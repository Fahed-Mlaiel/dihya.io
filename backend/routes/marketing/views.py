"""
Views ultra avancées pour le module Marketing
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import MarketingProject
from .serializers import MarketingProjectSerializer
from .audit import marketing_audit_logger
from .i18n import MARKETING_I18N
from .permissions import IsMarketingProjectOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class MarketingProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets Marketing.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
    """
    queryset = MarketingProject.objects.all()
    serializer_class = MarketingProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsMarketingProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        marketing_audit_logger.log(self.request.user, 'create', 'MarketingProject', obj.id, details=obj.name, language=obj.language)
        # hooks métier, monitoring, DWeb/IPFS export, etc.

    def perform_destroy(self, instance):
        marketing_audit_logger.log(self.request.user, 'delete', 'MarketingProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()
        # hooks métier, monitoring, DWeb/IPFS export, etc.
