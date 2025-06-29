# router.py – Routeur FastAPI ultra avancé pour Hotellerie

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/hotellerie")
def list_hotelleries():
    return {"hotelleries": [], "total": 0}


@router.post("/hotellerie")
def create_hotellerie(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
