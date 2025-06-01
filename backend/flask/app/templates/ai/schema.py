# schema.py - Dummy GraphQL-Schema für das AI-Modul
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(default_value="Hello AI GraphQL!")

ia_schema = Schema(query=Query)
