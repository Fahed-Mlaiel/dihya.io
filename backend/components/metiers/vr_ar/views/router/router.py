# router.py – Routeur FastAPI ultra avancé pour vr_ar

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/vr_ar")
def list_vr_ars():
    return {"vr_ars": [], "total": 0}


@router.post("/vr_ar")
def create_vr_ar(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
