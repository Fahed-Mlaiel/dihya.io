# URLs pour le module Assurance
from fastapi import APIRouter
from .views import get_assurance_view

router = APIRouter()

@router.get('/assurance')
def get_assurance():
    return get_assurance_view()

@router.get('/assurance/export')
def export_assurance():
    return {"export": True}

@router.get('/assurance/plugins')
def list_plugins():
    return {"plugins": ["audit", "rgpd", "ia"]}
