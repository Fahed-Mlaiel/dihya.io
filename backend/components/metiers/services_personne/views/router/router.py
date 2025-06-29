# router.py – Routeur FastAPI ultra avancé pour ServicesPersonne

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/services_personne")
def list_services_personnes():
    return {"services_personnes": [], "total": 0}


@router.post("/services_personne")
def create_services_personne(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
