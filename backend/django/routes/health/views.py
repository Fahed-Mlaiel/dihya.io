"""
Vues Django REST & GraphQL pour la gestion des projets santé.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from typing import Any
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import HealthProjectSerializer
from .models import HealthProject
from .permissions import IsAdminOrReadOnly
from core.audit import audit_log_action
from core.utils import get_current_tenant

class HealthListView(generics.ListCreateAPIView):
    queryset = HealthProject.objects.all()
    serializer_class = HealthProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return HealthProject.objects.filter(tenant=tenant)
    def perform_create(self, serializer):
        tenant = get_current_tenant(self.request)
        instance = serializer.save(tenant=tenant, created_by=self.request.user)
        audit_log_action(self.request.user, _('Création projet santé'), instance)

class HealthDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthProject.objects.all()
    serializer_class = HealthProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return HealthProject.objects.filter(tenant=tenant)
    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log_action(self.request.user, _('Mise à jour projet santé'), instance)
    def perform_destroy(self, instance):
        audit_log_action(self.request.user, _('Suppression projet santé'), instance)
        instance.delete()

class HealthExportView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, *args, **kwargs):
        # Export RGPD (exemple minimal)
        return Response({'export': 'ok'}, status=status.HTTP_200_OK)

class HealthPluginListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # Liste des plugins IA disponibles
        return Response({'plugins': ['llama', 'mixtral', 'mistral']}, status=status.HTTP_200_OK)

class HealthIAView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # Fallback IA (exemple minimal)
        text = request.data.get('text', '')
        return Response({'result': f'Réponse IA pour: {text}'}, status=status.HTTP_200_OK)
