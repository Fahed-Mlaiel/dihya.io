"""
Vues Django REST & GraphQL pour la gestion des projets banque/finance.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from typing import Any
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from .serializers import BanqueFinanceProjectSerializer
from .models import BanqueFinanceProject
from .permissions import IsAdminOrReadOnly
from .audit import audit_log_action
from .utils import get_current_tenant

class BanqueFinanceProjectViewSet(viewsets.ModelViewSet):
    """
    API avancée pour la gestion des projets banque/finance (REST & GraphQL-ready).
    """
    queryset = BanqueFinanceProject.objects.all()
    serializer_class = BanqueFinanceProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return BanqueFinanceProject.objects.filter(tenant=tenant)

    def perform_create(self, serializer):
        tenant = get_current_tenant(self.request)
        instance = serializer.save(tenant=tenant, created_by=self.request.user)
        audit_log_action(self.request.user, _('Création projet banque/finance'), instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log_action(self.request.user, _('Mise à jour projet banque/finance'), instance)

    def perform_destroy(self, instance):
        audit_log_action(self.request.user, _('Suppression projet banque/finance'), instance)
        instance.delete()
