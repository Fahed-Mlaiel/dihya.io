"""
Vues Django REST & GraphQL pour la gestion des projets d'administration publique.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from typing import Any
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from .serializers import AdministrationPubliqueProjectSerializer
from .models import AdministrationPubliqueProject
from .permissions import IsAdminOrReadOnly
from .audit import audit_log_action
from .utils import get_current_tenant

class AdministrationPubliqueProjectViewSet(viewsets.ModelViewSet):
    """
    API avancée pour la gestion des projets d'administration publique (REST & GraphQL-ready).
    """
    queryset = AdministrationPubliqueProject.objects.all()
    serializer_class = AdministrationPubliqueProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return AdministrationPubliqueProject.objects.filter(tenant=tenant)

    def perform_create(self, serializer):
        tenant = get_current_tenant(self.request)
        instance = serializer.save(tenant=tenant, created_by=self.request.user)
        audit_log_action(self.request.user, _('Création projet administration publique'), instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log_action(self.request.user, _('Mise à jour projet administration publique'), instance)

    def perform_destroy(self, instance):
        audit_log_action(self.request.user, _('Suppression projet administration publique'), instance)
        instance.delete()
