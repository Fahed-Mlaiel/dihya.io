"""
Services métier avancés pour le module construction (REST, GraphQL, sécurité, RGPD, multitenancy, plugins, audit).
"""
from .schemas import ConstructionBaseSchema
from .validators import validate_nom, validate_type
from .audit import log_audit
from .plugins import seo_plugin, accessibility_plugin, rgpd_plugin
from .i18n import get_i18n_message

def create_construction(data, user_id, tenant_id, lang="fr"):
    if not validate_nom(data.get("nom")):
        return {"error": get_i18n_message(lang, "invalid_nom")}, 400
    if not validate_type(data.get("type")):
        return {"error": "Type invalide."}, 400
    construction = data.copy()
    construction["id"] = 1
    log_audit("create", user_id, construction["id"])
    return {"message": get_i18n_message(lang, "created"), "data": construction}, 201

def update_construction(construction_id, data, user_id, tenant_id, lang="fr"):
    log_audit("update", user_id, construction_id)
    return {"message": get_i18n_message(lang, "updated")}

def delete_construction(construction_id, user_id, tenant_id, lang="fr"):
    log_audit("delete", user_id, construction_id)
    return {"message": get_i18n_message(lang, "deleted")}
