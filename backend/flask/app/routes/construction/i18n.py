"""
Internationalisation (i18n) pour le module construction (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Projet construction créé avec succès.",
        "updated": "Projet construction mis à jour.",
        "deleted": "Projet construction supprimé.",
        "not_found": "Projet construction introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Construction project successfully created.",
        "updated": "Construction project updated.",
        "deleted": "Construction project deleted.",
        "not_found": "Construction project not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء مشروع البناء بنجاح.",
        "updated": "تم تحديث مشروع البناء.",
        "deleted": "تم حذف مشروع البناء.",
        "not_found": "مشروع البناء غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
