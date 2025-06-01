"""
Internationalisation (i18n) pour le module culture (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Projet culturel créé avec succès.",
        "updated": "Projet culturel mis à jour.",
        "deleted": "Projet culturel supprimé.",
        "not_found": "Projet culturel introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Cultural project successfully created.",
        "updated": "Cultural project updated.",
        "deleted": "Cultural project deleted.",
        "not_found": "Cultural project not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء المشروع الثقافي بنجاح.",
        "updated": "تم تحديث المشروع الثقافي.",
        "deleted": "تم حذف المشروع الثقافي.",
        "not_found": "المشروع الثقافي غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
