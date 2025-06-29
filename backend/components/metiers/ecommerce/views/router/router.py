# router.py – Routeur FastAPI ultra avancé pour Ecommerce

from fastapi import APIRouter, status, Response

router = APIRouter()


@router.get("/ecommerce")
def list_ecommerces():
    return {"ecommerces": [], "total": 0}


@router.post("/ecommerce")
def create_ecommerce(data: dict, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return {
        "nom": data.get("nom", ""),
        "description": data.get("description", ""),
        "type": data.get("type", "objet"),
    }
