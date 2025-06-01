"""
Dihya – i18n pour le module Sécurité
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_incident': {
        'fr': _('Incident signalé avec succès.'),
        'en': _('Incident reported successfully.'),
        'ar': _('تم الإبلاغ عن الحادث بنجاح.'),
        'tzm': _('Yettwaselmed incident s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
