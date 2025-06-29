# router.py – Routeur FastAPI ultra avancé pour Energie

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/energie")
def list_energies():
    return {"energies": [], "total": 0}


@router.post("/energie")
def create_energie(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
