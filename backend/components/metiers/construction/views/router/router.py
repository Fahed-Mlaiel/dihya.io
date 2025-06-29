# router.py – Routeur FastAPI ultra avancé pour Construction

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/construction")
def list_constructions():
    return {"constructions": [], "total": 0}


@router.post("/construction")
def create_construction(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
