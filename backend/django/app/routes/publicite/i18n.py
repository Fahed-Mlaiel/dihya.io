"""
Dihya – i18n pour le module Publicité
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_create': {
        'fr': _('Campagne créée avec succès.'),
        'en': _('Campaign created successfully.'),
        'ar': _('تم إنشاء الحملة بنجاح.'),
        'tzm': _('Yettwaselmed campagne s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
