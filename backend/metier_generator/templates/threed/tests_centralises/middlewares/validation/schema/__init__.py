"""
Point d'entrée pour les tests du middleware validate_schema (Python)
"""
from .test_threed_schema import test_validate_schema_ok, test_validate_schema_no_schema

__all__ = ["test_validate_schema_ok", "test_validate_schema_no_schema"]
