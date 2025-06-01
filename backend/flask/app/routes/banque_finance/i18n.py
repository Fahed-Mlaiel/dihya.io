"""
Internationalisation (i18n) pour le module banque_finance (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Banque créée avec succès.",
        "updated": "Banque mise à jour.",
        "deleted": "Banque supprimée.",
        "not_found": "Banque introuvable.",
        "invalid_bic": "Le code BIC est invalide.",
    },
    "en": {
        "created": "Bank successfully created.",
        "updated": "Bank updated.",
        "deleted": "Bank deleted.",
        "not_found": "Bank not found.",
        "invalid_bic": "Invalid BIC code.",
    },
    "ar": {
        "created": "تم إنشاء البنك بنجاح.",
        "updated": "تم تحديث البنك.",
        "deleted": "تم حذف البنك.",
        "not_found": "البنك غير موجود.",
        "invalid_bic": "رمز BIC غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
