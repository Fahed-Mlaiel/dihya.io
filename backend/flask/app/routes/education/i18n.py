"""
Internationalisation (i18n) pour le module education (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Programme éducatif créé avec succès.",
        "updated": "Programme éducatif mis à jour.",
        "deleted": "Programme éducatif supprimé.",
        "not_found": "Programme éducatif introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Education program successfully created.",
        "updated": "Education program updated.",
        "deleted": "Education program deleted.",
        "not_found": "Education program not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء البرنامج التعليمي بنجاح.",
        "updated": "تم تحديث البرنامج التعليمي.",
        "deleted": "تم حذف البرنامج التعليمي.",
        "not_found": "البرنامج التعليمي غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
