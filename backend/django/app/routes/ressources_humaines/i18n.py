"""
Dihya – i18n pour le module Ressources Humaines
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_create': {
        'fr': _('Employé créé avec succès.'),
        'en': _('Employee created successfully.'),
        'ar': _('تم إنشاء الموظف بنجاح.'),
        'tzm': _('Yettwaselmed employé s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
