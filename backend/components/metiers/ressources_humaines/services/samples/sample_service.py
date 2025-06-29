"""
Service Python d'exemple ultra avancé pour Ressources_humaines, endpoints, logique métier, validation, audit, etc.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/samples/hello")
def hello_sample():
    """Endpoint de test ultra avancé."""
    return {"message": "Hello from Ressources_humaines sample service!"}


@router.post("/samples/validate")
def validate_sample(data: dict):
    """Validation avancée d'un échantillon."""
    if not data.get("value"):
        raise HTTPException(status_code=400, detail="Missing value")
    return {"validated": True, "input": data}
