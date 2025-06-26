# router.py – Routeur FastAPI ultra avancé pour Crypto

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/crypto")
def list_cryptos():
    return {"cryptos": [], "total": 0}


@router.post("/crypto")
def create_crypto(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
