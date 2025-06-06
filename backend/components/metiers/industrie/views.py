"""
Vues avancées pour le module Environnement
Expose les routes API RESTful, la logique métier, et l'intégration avec les schémas et plugins.
"""
from fastapi import APIRouter, HTTPException, status
from .schemas import EnvironnementInDB, EnvironnementList, EnvironnementCreate, EnvironnementUpdate
from typing import List

router = APIRouter()

environnements_db: List[EnvironnementInDB] = []

@router.get("/environnements", response_model=EnvironnementList)
def list_environnements():
    return {"environnements": environnements_db, "total": len(environnements_db)}

@router.post("/environnements", response_model=EnvironnementInDB, status_code=status.HTTP_201_CREATED)
def create_environnement(env: EnvironnementCreate):
    new_env = EnvironnementInDB(id=len(environnements_db)+1, **env.dict())
    environnements_db.append(new_env)
    return new_env

@router.get("/environnements/{env_id}", response_model=EnvironnementInDB)
def get_environnement(env_id: int):
    for env in environnements_db:
        if env.id == env_id:
            return env
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Environnement non trouvé")

@router.put("/environnements/{env_id}", response_model=EnvironnementInDB)
def update_environnement(env_id: int, env: EnvironnementUpdate):
    for i, e in enumerate(environnements_db):
        if e.id == env_id:
            updated = e.copy(update=env.dict(exclude_unset=True))
            environnements_db[i] = updated
            return updated
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Environnement non trouvé")

@router.delete("/environnements/{env_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_environnement(env_id: int):
    global environnements_db
    environnements_db = [e for e in environnements_db if e.id != env_id]
    return
