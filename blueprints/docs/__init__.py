"""
Initialisation des blueprints Docs (Python)
Exporte tous les générateurs de documentation métiers : OpenAPI, guides d’intégration, docstring, validation, etc.
"""
from .api_reference import *
from .integration_guide import *

__all__ = ['api_reference', 'integration_guide']

# Exemple d’utilisation :
# from blueprints.docs import api_reference, integration_guide
# api_reference.generate_openapi_doc(...)
# integration_guide.generate_integration_guide(...)
