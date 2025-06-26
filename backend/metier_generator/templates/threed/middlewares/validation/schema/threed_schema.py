"""
Middleware de validation de schéma pour le module threed.
Valide un dictionnaire data selon un schéma JSON Schema simplifié.
"""


def validate_schema(schema, data):
    if not schema or not isinstance(schema, dict):
        return False
    # Validation ultra simplifiée pour l’exemple
    if schema.get("type") == "object":
        props = schema.get("properties", {})
        for key, prop in props.items():
            if prop.get("type") == "string" and not isinstance(data.get(key), str):
                return False
    return True
