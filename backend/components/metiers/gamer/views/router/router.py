# router.py – Routeur FastAPI ultra avancé pour Gamer

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/gamer")
def list_gamers():
    return {"gamers": [], "total": 0}


@router.post("/gamer")
def create_gamer(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
