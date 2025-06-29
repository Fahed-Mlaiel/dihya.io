# router.py – Routeur FastAPI ultra avancé pour Sport

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/sport")
def list_sports():
    return {"sports": [], "total": 0}


@router.post("/sport")
def create_sport(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
