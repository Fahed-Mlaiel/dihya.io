# router.py – Routeur FastAPI ultra avancé pour Tourisme

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/tourisme")
def list_tourismes():
    return {"tourismes": [], "total": 0}


@router.post("/tourisme")
def create_tourisme(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
