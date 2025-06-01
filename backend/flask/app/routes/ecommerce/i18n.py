"""
Internationalisation (i18n) pour le module ecommerce (fr, en, ar, etc.).
"""
I18N = {
    "fr": {
        "created": "Boutique ecommerce créée avec succès.",
        "updated": "Boutique ecommerce mise à jour.",
        "deleted": "Boutique ecommerce supprimée.",
        "not_found": "Boutique ecommerce introuvable.",
        "invalid_nom": "Le nom est invalide.",
    },
    "en": {
        "created": "Ecommerce store successfully created.",
        "updated": "Ecommerce store updated.",
        "deleted": "Ecommerce store deleted.",
        "not_found": "Ecommerce store not found.",
        "invalid_nom": "Invalid name.",
    },
    "ar": {
        "created": "تم إنشاء المتجر الإلكتروني بنجاح.",
        "updated": "تم تحديث المتجر الإلكتروني.",
        "deleted": "تم حذف المتجر الإلكتروني.",
        "not_found": "المتجر الإلكتروني غير موجود.",
        "invalid_nom": "الاسم غير صالح.",
    }
}

def get_i18n_message(lang, key):
    return I18N.get(lang, I18N["fr"]).get(key, key)
