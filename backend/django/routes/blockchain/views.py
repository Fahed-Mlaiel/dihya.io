"""
Vues RESTful et GraphQL pour la gestion de projets blockchain (crypto, NFT, smart contracts, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blockchain
from .serializers import BlockchainSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class BlockchainListView(generics.ListCreateAPIView):
    """Liste et création de projets blockchain (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Blockchain.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'blockchain')
        return super().list(request, *args, **kwargs)

class BlockchainDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet blockchain (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Blockchain.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'blockchain')
        return super().retrieve(request, *args, **kwargs)

class BlockchainExportView(APIView):
    """Export des projets blockchain (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'blockchain')
        return export_projects_zip(Blockchain, tenant)

class BlockchainPluginListView(APIView):
    """Liste des plugins blockchain (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'blockchain')
        return Response(get_plugins('blockchain'))

class BlockchainIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'blockchain')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class BlockchainType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    blockchain = graphene.Field(BlockchainType, id=graphene.Int())
    all_blockchain = graphene.List(BlockchainType)

    def resolve_blockchain(self, info, id):
        try:
            obj = Blockchain.objects.get(pk=id)
            return BlockchainType(id=obj.id, name=obj.name, description=obj.description)
        except Blockchain.DoesNotExist:
            raise GraphQLError(_('Projet blockchain introuvable'))

    def resolve_all_blockchain(self, info):
        return [BlockchainType(id=obj.id, name=obj.name, description=obj.description) for obj in Blockchain.objects.all()]

schema = graphene.Schema(query=Query)
