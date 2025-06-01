"""
Dihya – i18n pour le module Médias
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_upload': {
        'fr': _('Média téléchargé avec succès.'),
        'en': _('Media uploaded successfully.'),
        'ar': _('تم تحميل الوسائط بنجاح.'),
        'tzm': _('Yettwaselmed umedia s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
