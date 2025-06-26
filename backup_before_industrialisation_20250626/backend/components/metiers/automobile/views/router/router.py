# router.py – Routeur FastAPI ultra avancé pour Automobile

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/automobile")
def list_automobiles():
    return {"automobiles": [], "total": 0}


@router.post("/automobile")
def create_automobile(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
