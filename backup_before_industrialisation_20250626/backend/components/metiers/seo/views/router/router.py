# router.py – Routeur FastAPI ultra avancé pour Seo

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/seo")
def list_seos():
    return {"seos": [], "total": 0}


@router.post("/seo")
def create_seo(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
