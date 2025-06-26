# router.py – Routeur FastAPI ultra avancé pour Education

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/education")
def list_educations():
    return {"educations": [], "total": 0}


@router.post("/education")
def create_education(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
