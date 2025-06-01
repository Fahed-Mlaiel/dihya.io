"""
Vues Django REST & GraphQL pour la gestion des projets industriels.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from typing import Any
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import IndustrieProjectSerializer
from .models import IndustrieProject
from .permissions import IsAdminOrReadOnly
from core.audit import audit_log_action
from core.utils import get_current_tenant

class IndustrieListView(generics.ListCreateAPIView):
    queryset = IndustrieProject.objects.all()
    serializer_class = IndustrieProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return IndustrieProject.objects.filter(tenant=tenant)
    def perform_create(self, serializer):
        tenant = get_current_tenant(self.request)
        instance = serializer.save(tenant=tenant, created_by=self.request.user)
        audit_log_action(self.request.user, _('Création projet industriel'), instance)

class IndustrieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustrieProject.objects.all()
    serializer_class = IndustrieProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return IndustrieProject.objects.filter(tenant=tenant)
    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log_action(self.request.user, _('Mise à jour projet industriel'), instance)
    def perform_destroy(self, instance):
        audit_log_action(self.request.user, _('Suppression projet industriel'), instance)
        instance.delete()

class IndustrieExportView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, *args, **kwargs):
        # Export RGPD (exemple minimal)
        return Response({'export': 'ok'}, status=status.HTTP_200_OK)

class IndustriePluginListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # Liste des plugins IA disponibles
        return Response({'plugins': ['llama', 'mixtral', 'mistral']}, status=status.HTTP_200_OK)

class IndustrieIAView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        # Fallback IA (exemple minimal)
        text = request.data.get('text', '')
        return Response({'result': f'Réponse IA pour: {text}'}, status=status.HTTP_200_OK)
