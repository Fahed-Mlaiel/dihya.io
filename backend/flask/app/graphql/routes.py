"""
GraphQL API routes for Dihya Coding (Flask).
"""
from flask import Blueprint
from backend.flask.app.graphql.schema import schema
from flask_graphql import GraphQLView

graphql_bp = Blueprint('graphql', __name__)

graphql_bp.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

__all__ = ["graphql_bp"]
