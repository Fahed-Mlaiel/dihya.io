"""
Internationalisation (i18n) pour le module energie (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Projet énergie créé avec succès.",
        "updated": "Projet énergie mis à jour.",
        "deleted": "Projet énergie supprimé.",
        "not_found": "Projet énergie introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Energy project successfully created.",
        "updated": "Energy project updated.",
        "deleted": "Energy project deleted.",
        "not_found": "Energy project not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء مشروع الطاقة بنجاح.",
        "updated": "تم تحديث مشروع الطاقة.",
        "deleted": "تم حذف مشروع الطاقة.",
        "not_found": "مشروع الطاقة غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
