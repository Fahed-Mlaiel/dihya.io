# router.py – Routeur FastAPI ultra avancé pour Arts

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/arts")
def list_artss():
    return {"artss": [], "total": 0}


@router.post("/arts")
def create_arts(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
