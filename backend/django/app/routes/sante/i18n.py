"""
Dihya – i18n pour le module Santé
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_patient': {
        'fr': _('Patient enregistré avec succès.'),
        'en': _('Patient registered successfully.'),
        'ar': _('تم تسجيل المريض بنجاح.'),
        'tzm': _('Yettwaselmed patient s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
