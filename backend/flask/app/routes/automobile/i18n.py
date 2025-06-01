"""
Internationalisation (i18n) pour le module automobile (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Automobile créée avec succès.",
        "updated": "Automobile mise à jour.",
        "deleted": "Automobile supprimée.",
        "not_found": "Automobile introuvable.",
        "invalid_vin": "Le VIN est invalide.",
    },
    "en": {
        "created": "Automobile successfully created.",
        "updated": "Automobile updated.",
        "deleted": "Automobile deleted.",
        "not_found": "Automobile not found.",
        "invalid_vin": "Invalid VIN.",
    },
    "ar": {
        "created": "تم إنشاء السيارة بنجاح.",
        "updated": "تم تحديث السيارة.",
        "deleted": "تم حذف السيارة.",
        "not_found": "السيارة غير موجودة.",
        "invalid_vin": "رقم الهيكل غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
