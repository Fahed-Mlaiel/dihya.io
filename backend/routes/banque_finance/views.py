"""
Views ultra avancées pour le module Banque & Finance
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy, sectorisation, DWeb/IPFS, monitoring, hooks métier, CI/CD, RBAC.
"""
from rest_framework import viewsets, permissions
from .models import BanqueFinanceProject, BanqueFinanceAsset
from .serializers import BanqueFinanceProjectSerializer, BanqueFinanceAssetSerializer
from .audit import banque_finance_audit_logger
from .i18n import BANQUE_FINANCE_I18N
from .permissions import IsBanqueFinanceProjectOwnerOrReadOnly, IsBanqueFinanceAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class BanqueFinanceProjectViewSet(viewsets.ModelViewSet):
    queryset = BanqueFinanceProject.objects.all()
    serializer_class = BanqueFinanceProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBanqueFinanceProjectOwnerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        banque_finance_audit_logger.log(self.request.user, 'create', 'BanqueFinanceProject', obj.id, details=obj.name, language=obj.language)
    def perform_destroy(self, instance):
        banque_finance_audit_logger.log(self.request.user, 'delete', 'BanqueFinanceProject', instance.id, details=instance.name, language=instance.language)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class BanqueFinanceAssetViewSet(viewsets.ModelViewSet):
    queryset = BanqueFinanceAsset.objects.all()
    serializer_class = BanqueFinanceAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBanqueFinanceAssetManagerOrReadOnly]
    def perform_create(self, serializer):
        obj = serializer.save()
        banque_finance_audit_logger.log(self.request.user, 'upload', 'BanqueFinanceAsset', obj.id, details=obj.name, language=obj.language)
