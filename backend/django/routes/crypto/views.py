"""
Vues RESTful et GraphQL pour la gestion de projets crypto (échanges, wallets, DeFi, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Crypto
from .serializers import CryptoSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class CryptoListView(generics.ListCreateAPIView):
    """Liste et création de projets crypto (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Crypto.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'crypto')
        return super().list(request, *args, **kwargs)

class CryptoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet crypto (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Crypto.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'crypto')
        return super().retrieve(request, *args, **kwargs)

class CryptoExportView(APIView):
    """Export des projets crypto (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'crypto')
        return export_projects_zip(Crypto, tenant)

class CryptoPluginListView(APIView):
    """Liste des plugins crypto (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'crypto')
        return Response(get_plugins('crypto'))

class CryptoIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'crypto')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class CryptoType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    crypto = graphene.Field(CryptoType, id=graphene.Int())
    all_crypto = graphene.List(CryptoType)

    def resolve_crypto(self, info, id):
        try:
            obj = Crypto.objects.get(pk=id)
            return CryptoType(id=obj.id, name=obj.name, description=obj.description)
        except Crypto.DoesNotExist:
            raise GraphQLError(_('Projet crypto introuvable'))

    def resolve_all_crypto(self, info):
        return [CryptoType(id=obj.id, name=obj.name, description=obj.description) for obj in Crypto.objects.all()]

schema = graphene.Schema(query=Query)
