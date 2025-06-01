"""
graphql.py - Schémas GraphQL pour Dihya (routes IA, utils, etc.)
"""
from graphene import ObjectType, String, Schema

class QueryIA(ObjectType):
    hello = String(description="Test GraphQL IA")
    def resolve_hello(self, info):
        return "Hello IA GraphQL!"

graphql_ia_schema = Schema(query=QueryIA)

class QueryUtils(ObjectType):
    ping = String(description="Test GraphQL utils")
    def resolve_ping(self, info):
        return "pong"

graphql_utils_schema = Schema(query=QueryUtils)
