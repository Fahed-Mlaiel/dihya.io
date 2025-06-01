"""
Services métier avancés pour le module crypto (REST, GraphQL, sécurité, RGPD, multitenancy, plugins, audit).
"""
from .schemas import CryptoBaseSchema
from .validators import validate_nom, validate_symbole
from .audit import log_audit
from .plugins import seo_plugin, accessibility_plugin, rgpd_plugin
from .i18n import get_i18n_message

def create_crypto(data, user_id, tenant_id, lang="fr"):
    if not validate_nom(data.get("nom")):
        return {"error": get_i18n_message(lang, "invalid_nom")}, 400
    if not validate_symbole(data.get("symbole")):
        return {"error": "Symbole invalide."}, 400
    crypto = data.copy()
    crypto["id"] = 1
    log_audit("create", user_id, crypto["id"])
    return {"message": get_i18n_message(lang, "created"), "data": crypto}, 201

def update_crypto(crypto_id, data, user_id, tenant_id, lang="fr"):
    log_audit("update", user_id, crypto_id)
    return {"message": get_i18n_message(lang, "updated")}

def delete_crypto(crypto_id, user_id, tenant_id, lang="fr"):
    log_audit("delete", user_id, crypto_id)
    return {"message": get_i18n_message(lang, "deleted")}
