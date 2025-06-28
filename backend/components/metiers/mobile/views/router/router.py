# router.py – Routeur FastAPI ultra avancé pour Mobile

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/mobile")
def list_mobiles():
    return {"mobiles": [], "total": 0}


@router.post("/mobile")
def create_mobile(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
