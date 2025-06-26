# router.py – Routeur FastAPI ultra avancé pour Voyage

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/voyage")
def list_voyages():
    return {"voyages": [], "total": 0}


@router.post("/voyage")
def create_voyage(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
