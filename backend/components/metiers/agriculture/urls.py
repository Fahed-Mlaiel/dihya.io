# URLs pour Agriculture

from fastapi import APIRouter

router = APIRouter()

@router.get("/agriculture")
def get_agriculture():
    return {"message": "Bienvenue dans Agriculture"}

@router.get("/agriculture/export_rgpd")
def export_rgpd():
    return {"export": True, "rgpd": "conforme"}

@router.get("/agriculture/plugins/list")
def list_plugins():
    return {"plugins": ["SampleAgriculturePlugin"]}
