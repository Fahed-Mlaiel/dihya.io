"""
Blueprint documentation API Reference (Python)
Génération de documentation OpenAPI avancée, sections dynamiques, validation de schémas, doc interactive.
"""
import yaml
from typing import Dict, Any

def generate_openapi_doc(title: str, version: str, endpoints: Dict[str, Any]) -> str:
    """
    Génère un schéma OpenAPI YAML à partir des endpoints fournis.
    """
    openapi = {
        "openapi": "3.0.0",
        "info": {"title": title, "version": version},
        "paths": endpoints
    }
    return yaml.dump(openapi, allow_unicode=True)

# Exemple d'utilisation :
# endpoints = {"/assets": {"get": {"summary": "Liste des assets"}}}
# print(generate_openapi_doc("Inventaire API", "1.0.0", endpoints))
