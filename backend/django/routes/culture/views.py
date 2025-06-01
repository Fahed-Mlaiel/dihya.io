"""
Vues RESTful et GraphQL pour la gestion de projets culturels (événements, patrimoine, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Culture
from .serializers import CultureSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class CultureListView(generics.ListCreateAPIView):
    """Liste et création de projets culturels (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Culture.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'culture')
        return super().list(request, *args, **kwargs)

class CultureDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet culturel (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Culture.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'culture')
        return super().retrieve(request, *args, **kwargs)

class CultureExportView(APIView):
    """Export des projets culturels (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'culture')
        return export_projects_zip(Culture, tenant)

class CulturePluginListView(APIView):
    """Liste des plugins culturels (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'culture')
        return Response(get_plugins('culture'))

class CultureIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'culture')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class CultureType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    culture = graphene.Field(CultureType, id=graphene.Int())
    all_culture = graphene.List(CultureType)

    def resolve_culture(self, info, id):
        try:
            obj = Culture.objects.get(pk=id)
            return CultureType(id=obj.id, name=obj.name, description=obj.description)
        except Culture.DoesNotExist:
            raise GraphQLError(_('Projet culturel introuvable'))

    def resolve_all_culture(self, info):
        return [CultureType(id=obj.id, name=obj.name, description=obj.description) for obj in Culture.objects.all()]

schema = graphene.Schema(query=Query)
