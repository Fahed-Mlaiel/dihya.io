# router.py – Routeur FastAPI ultra avancé pour Securite

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/securite")
def list_securites():
    return {"securites": [], "total": 0}


@router.post("/securite")
def create_securite(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
