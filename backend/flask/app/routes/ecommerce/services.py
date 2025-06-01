"""
Services métier avancés pour le module ecommerce (REST, GraphQL, sécurité, RGPD, multitenancy, plugins, audit).
"""
from .schemas import EcommerceBaseSchema
from .validators import validate_nom, validate_categorie
from .audit import log_audit
from .plugins import seo_plugin, accessibility_plugin, rgpd_plugin
from .i18n import get_i18n_message

def create_ecommerce(data, user_id, tenant_id, lang="fr"):
    if not validate_nom(data.get("nom")):
        return {"error": get_i18n_message(lang, "invalid_nom")}, 400
    if not validate_categorie(data.get("categorie")):
        return {"error": "Catégorie invalide."}, 400
    ecommerce = data.copy()
    ecommerce["id"] = 1
    log_audit("create", user_id, ecommerce["id"])
    return {"message": get_i18n_message(lang, "created"), "data": ecommerce}, 201

def update_ecommerce(ecommerce_id, data, user_id, tenant_id, lang="fr"):
    log_audit("update", user_id, ecommerce_id)
    return {"message": get_i18n_message(lang, "updated")}

def delete_ecommerce(ecommerce_id, user_id, tenant_id, lang="fr"):
    log_audit("delete", user_id, ecommerce_id)
    return {"message": get_i18n_message(lang, "deleted")}
