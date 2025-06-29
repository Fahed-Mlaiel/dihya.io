# router.py – Routeur FastAPI ultra avancé pour voice

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/voice")
def list_voices():
    return {"voices": [], "total": 0}


@router.post("/voice")
def create_voice(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
