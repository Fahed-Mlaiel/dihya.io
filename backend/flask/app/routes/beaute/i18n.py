"""
Internationalisation (i18n) pour le module beaute (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Entrée beauté créée avec succès.",
        "updated": "Entrée beauté mise à jour.",
        "deleted": "Entrée beauté supprimée.",
        "not_found": "Entrée beauté introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Beauty entry successfully created.",
        "updated": "Beauty entry updated.",
        "deleted": "Beauty entry deleted.",
        "not_found": "Beauty entry not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء عنصر الجمال بنجاح.",
        "updated": "تم تحديث عنصر الجمال.",
        "deleted": "تم حذف عنصر الجمال.",
        "not_found": "عنصر الجمال غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
