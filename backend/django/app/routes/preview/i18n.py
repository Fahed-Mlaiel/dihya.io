"""
Dihya – i18n pour le module Preview
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_preview': {
        'fr': _('Aperçu généré avec succès.'),
        'en': _('Preview generated successfully.'),
        'ar': _('تم إنشاء المعاينة بنجاح.'),
        'tzm': _('Yettwaselmed preview s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
