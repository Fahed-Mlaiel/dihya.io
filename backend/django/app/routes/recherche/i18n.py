"""
Dihya – i18n pour le module Recherche
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_search': {
        'fr': _('Recherche effectuée avec succès.'),
        'en': _('Search completed successfully.'),
        'ar': _('تمت عملية البحث بنجاح.'),
        'tzm': _('Yettwaselmed recherche s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
