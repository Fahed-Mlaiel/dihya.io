"""
Internationalisation (i18n) pour le module btp (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Entrée BTP créée avec succès.",
        "updated": "Entrée BTP mise à jour.",
        "deleted": "Entrée BTP supprimée.",
        "not_found": "Entrée BTP introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "BTP entry successfully created.",
        "updated": "BTP entry updated.",
        "deleted": "BTP entry deleted.",
        "not_found": "BTP entry not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء عنصر البناء بنجاح.",
        "updated": "تم تحديث عنصر البناء.",
        "deleted": "تم حذف عنصر البناء.",
        "not_found": "عنصر البناء غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
