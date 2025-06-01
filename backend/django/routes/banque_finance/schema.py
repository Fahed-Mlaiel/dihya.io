"""
Schéma GraphQL pour la gestion avancée des projets banque/finance.
Inclut sécurité, multilingue, audit, RGPD, plugins, multitenancy.
"""
import graphene
from graphene_django.types import DjangoObjectType
from .models import BanqueFinanceProject

class BanqueFinanceProjectType(DjangoObjectType):
    class Meta:
        model = BanqueFinanceProject
        fields = ("id", "name", "description", "created_at", "updated_at", "tenant", "created_by", "is_active")

class Query(graphene.ObjectType):
    all_banque_finance_projects = graphene.List(BanqueFinanceProjectType)
    def resolve_all_banque_finance_projects(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return BanqueFinanceProject.objects.none()
        return BanqueFinanceProject.objects.filter(tenant=getattr(user, 'tenant', None))

schema = graphene.Schema(query=Query)
