"""
Dihya – i18n pour le module Science
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_projet': {
        'fr': _('Projet scientifique enregistré avec succès.'),
        'en': _('Scientific project registered successfully.'),
        'ar': _('تم تسجيل المشروع العلمي بنجاح.'),
        'tzm': _('Yettwaselmed projet scientifique s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
