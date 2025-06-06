# api.py – Point d’entrée FastAPI ultra avancé pour l’API Threed (Python)
from fastapi import APIRouter, HTTPException, Request
from backend.components.metiers.threed.api.core.controllers.threed_controller import ThreedController
from backend.components.metiers.threed.api.core.middlewares.middlewares import rgpd_middleware, accessibility_middleware, audit_request
from backend.components.metiers.threed.api.core.rgpd.rgpd import rgpd_sanitize
from backend.components.metiers.threed.api.core.accessibility.accessibility import check_accessibility
from backend.components.metiers.threed.api.core.audit.audit import audit_entity
from backend.components.metiers.threed.api.core.hooks.hooks import before_action, after_action

router = APIRouter()

@router.middleware('http')
async def rgpd_middleware_wrapper(request: Request, call_next):
    response = await rgpd_middleware(request, call_next)
    return response

@router.middleware('http')
async def accessibility_middleware_wrapper(request: Request, call_next):
    response = await accessibility_middleware(request, call_next)
    return response

@router.middleware('http')
async def audit_request_wrapper(request: Request, call_next):
    response = await audit_request(request, call_next)
    return response

@router.get('/threed/{id}')
async def get_threed(id: str):
    before_action('read', {'id': id})
    entity = ThreedController.get_by_id(id)
    if not entity:
        raise HTTPException(status_code=404, detail='Not found')
    entity = rgpd_sanitize(entity)
    check_accessibility(entity)
    audit_entity(entity, 'read')
    after_action('read', entity)
    return entity

@router.post('/threed')
async def create_threed(data: dict):
    before_action('create', data)
    created = ThreedController.create(data)
    audit_entity(created, 'create')
    after_action('create', created)
    return rgpd_sanitize(created)

@router.put('/threed/{id}')
async def update_threed(id: str, data: dict):
    before_action('update', {'id': id, **data})
    updated = ThreedController.update(id, data)
    audit_entity(updated, 'update')
    after_action('update', updated)
    return rgpd_sanitize(updated)

@router.delete('/threed/{id}')
async def delete_threed(id: str):
    before_action('delete', {'id': id})
    deleted = ThreedController.delete(id)
    audit_entity({'id': id}, 'delete')
    after_action('delete', {'id': id})
    return {'deleted': deleted}
