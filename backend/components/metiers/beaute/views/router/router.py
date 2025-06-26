# router.py – Routeur FastAPI ultra avancé pour Beaute

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/beaute")
def list_beautes():
    return {"beautes": [], "total": 0}


@router.post("/beaute")
def create_beaute(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
