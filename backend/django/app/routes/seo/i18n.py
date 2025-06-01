"""
Dihya – i18n pour le module SEO
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_audit': {
        'fr': _('Audit SEO réalisé avec succès.'),
        'en': _('SEO audit completed successfully.'),
        'ar': _('تم إجراء تدقيق SEO بنجاح.'),
        'tzm': _('Yettwaselmed audit SEO s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
