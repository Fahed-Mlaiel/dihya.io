# router.py – Routeur FastAPI ultra avancé pour Immobilier

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/immobilier")
def list_immobiliers():
    return {"immobiliers": [], "total": 0}


@router.post("/immobilier")
def create_immobilier(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
