# router.py – Routeur FastAPI ultra avancé pour Science

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/science")
def list_sciences():
    return {"sciences": [], "total": 0}


@router.post("/science")
def create_science(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
