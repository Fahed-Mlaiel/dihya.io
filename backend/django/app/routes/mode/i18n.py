"""
Dihya – i18n pour le module Mode
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_create': {
        'fr': _('Création réussie.'),
        'en': _('Successfully created.'),
        'ar': _('تم الإنشاء بنجاح.'),
        'tzm': _('Yettwaselmed s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
