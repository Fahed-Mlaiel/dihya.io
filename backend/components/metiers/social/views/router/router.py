# router.py – Routeur FastAPI ultra avancé pour Social

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/social")
def list_socials():
    return {"socials": [], "total": 0}


@router.post("/social")
def create_social(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
