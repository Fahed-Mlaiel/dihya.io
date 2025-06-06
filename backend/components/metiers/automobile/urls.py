# URLs automobile ultra avancées (exemple pour FastAPI)
from fastapi import APIRouter
from .views import afficher_automobile

router = APIRouter()

@router.get('/automobile')
def get_automobile():
    return {"message": afficher_automobile('Voiture électrique', 'actif', 'Alice')}
