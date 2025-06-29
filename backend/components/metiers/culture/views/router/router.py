# router.py – Routeur FastAPI ultra avancé pour Culture

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/culture")
def list_cultures():
    return {"cultures": [], "total": 0}


@router.post("/culture")
def create_culture(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
