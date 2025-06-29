"""
Blueprint validation métier Asset (Python)
Validation ultra avancée : synchrones/asynchrones, reporting, extension, doc, exemples.
"""
from typing import Dict, Any

def validate_asset(asset: Dict[str, Any]) -> Dict[str, Any]:
    """Valide un asset : nom obligatoire, reporting détaillé, extension métier."""
    errors = []
    if not asset.get('name'):
        errors.append('Le nom est obligatoire')
    is_valid = not errors
    return {"valid": is_valid, "errors": errors, **asset}

async def async_validate_asset(asset: Dict[str, Any]) -> Dict[str, Any]:
    return validate_asset(asset)

# Exemple d’utilisation :
# print(validate_asset({"id": 1, "name": "Ordinateur"}))
# print(validate_asset({"id": 2}))
