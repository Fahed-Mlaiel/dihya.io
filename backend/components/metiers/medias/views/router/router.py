# router.py – Routeur FastAPI ultra avancé pour Medias

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/medias")
def list_mediass():
    return {"mediass": [], "total": 0}


@router.post("/medias")
def create_medias(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
