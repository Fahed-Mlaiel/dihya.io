# router.py – Routeur FastAPI ultra avancé pour Transport

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/transport")
def list_transports():
    return {"transports": [], "total": 0}


@router.post("/transport")
def create_transport(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
