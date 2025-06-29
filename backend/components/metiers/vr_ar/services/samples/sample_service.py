"""
Service Python d'exemple ultra avancé pour vr_ar, endpoints, logique métier, validation, audit, etc.
"""

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/samples/hello")
def hello_sample():
    """Endpoint de test ultra avancé."""
    return {"message": "Hello from vr_ar sample service!"}


@router.post("/samples/validate")
def validate_sample(data: dict):
    """Validation avancée d'un échantillon."""
    if not data.get("value"):
        raise HTTPException(status_code=400, detail="Missing value")
    return {"validated": True, "input": data}
