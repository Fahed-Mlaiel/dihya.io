"""
Internationalisation (i18n) pour le module blockchain (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Blockchain créée avec succès.",
        "updated": "Blockchain mise à jour.",
        "deleted": "Blockchain supprimée.",
        "not_found": "Blockchain introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Blockchain successfully created.",
        "updated": "Blockchain updated.",
        "deleted": "Blockchain deleted.",
        "not_found": "Blockchain not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء البلوكشين بنجاح.",
        "updated": "تم تحديث البلوكشين.",
        "deleted": "تم حذف البلوكشين.",
        "not_found": "البلوكشين غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
