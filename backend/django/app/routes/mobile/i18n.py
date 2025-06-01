"""
Dihya – i18n pour le module Mobile
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_register': {
        'fr': _('Appareil enregistré avec succès.'),
        'en': _('Device registered successfully.'),
        'ar': _('تم تسجيل الجهاز بنجاح.'),
        'tzm': _('Yettwaselmed device s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
