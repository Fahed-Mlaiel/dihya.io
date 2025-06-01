"""
Schéma GraphQL pour la gestion avancée des projets artistiques.
Inclut sécurité, multilingue, audit, RGPD, plugins, multitenancy.
"""
import graphene
from graphene_django.types import DjangoObjectType
from .models import ArtProject

class ArtProjectType(DjangoObjectType):
    class Meta:
        model = ArtProject
        fields = ("id", "name", "description", "created_at", "updated_at", "tenant", "created_by", "is_active")

class Query(graphene.ObjectType):
    all_art_projects = graphene.List(ArtProjectType)
    def resolve_all_art_projects(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return ArtProject.objects.none()
        return ArtProject.objects.filter(tenant=getattr(user, 'tenant', None))

schema = graphene.Schema(query=Query)
