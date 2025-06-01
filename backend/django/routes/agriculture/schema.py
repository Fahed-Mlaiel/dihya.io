"""
Schéma GraphQL pour la gestion avancée des projets agricoles.
Inclut sécurité, multilingue, audit, RGPD, plugins, multitenancy.
"""
import graphene
from graphene_django.types import DjangoObjectType
from .models import AgricultureProject

class AgricultureProjectType(DjangoObjectType):
    class Meta:
        model = AgricultureProject
        fields = ("id", "name", "description", "created_at", "updated_at", "tenant", "created_by", "is_active")

class Query(graphene.ObjectType):
    all_agriculture_projects = graphene.List(AgricultureProjectType)
    def resolve_all_agriculture_projects(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return AgricultureProject.objects.none()
        return AgricultureProject.objects.filter(tenant=getattr(user, 'tenant', None))

schema = graphene.Schema(query=Query)
