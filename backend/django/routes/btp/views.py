"""
Vues RESTful et GraphQL pour la gestion de projets BTP (bâtiment, travaux publics, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BTP
from .serializers import BTPSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class BTPListView(generics.ListCreateAPIView):
    """Liste et création de projets BTP (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = BTP.objects.all()
    serializer_class = BTPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return BTP.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'btp')
        return super().list(request, *args, **kwargs)

class BTPDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet BTP (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = BTP.objects.all()
    serializer_class = BTPSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return BTP.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'btp')
        return super().retrieve(request, *args, **kwargs)

class BTPExportView(APIView):
    """Export des projets BTP (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'btp')
        return export_projects_zip(BTP, tenant)

class BTPPluginListView(APIView):
    """Liste des plugins BTP (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'btp')
        return Response(get_plugins('btp'))

class BTPIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'btp')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class BTPType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    btp = graphene.Field(BTPType, id=graphene.Int())
    all_btp = graphene.List(BTPType)

    def resolve_btp(self, info, id):
        try:
            obj = BTP.objects.get(pk=id)
            return BTPType(id=obj.id, name=obj.name, description=obj.description)
        except BTP.DoesNotExist:
            raise GraphQLError(_('Projet BTP introuvable'))

    def resolve_all_btp(self, info):
        return [BTPType(id=obj.id, name=obj.name, description=obj.description) for obj in BTP.objects.all()]

schema = graphene.Schema(query=Query)
