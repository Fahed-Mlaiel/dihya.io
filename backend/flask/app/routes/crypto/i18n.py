"""
Internationalisation (i18n) pour le module crypto (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Crypto créée avec succès.",
        "updated": "Crypto mise à jour.",
        "deleted": "Crypto supprimée.",
        "not_found": "Crypto introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Crypto successfully created.",
        "updated": "Crypto updated.",
        "deleted": "Crypto deleted.",
        "not_found": "Crypto not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء العملة الرقمية بنجاح.",
        "updated": "تم تحديث العملة الرقمية.",
        "deleted": "تم حذف العملة الرقمية.",
        "not_found": "العملة الرقمية غير موجودة.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
