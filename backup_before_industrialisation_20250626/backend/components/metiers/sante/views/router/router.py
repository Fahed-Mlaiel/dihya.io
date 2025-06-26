# router.py – Routeur FastAPI ultra avancé pour Sante

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/sante")
def list_santes():
    return {"santes": [], "total": 0}


@router.post("/sante")
def create_sante(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
