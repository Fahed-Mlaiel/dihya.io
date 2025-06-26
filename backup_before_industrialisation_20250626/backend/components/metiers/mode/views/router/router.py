# router.py – Routeur FastAPI ultra avancé pour Mode

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/mode")
def list_modes():
    return {"modes": [], "total": 0}


@router.post("/mode")
def create_mode(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
