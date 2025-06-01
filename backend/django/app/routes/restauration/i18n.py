"""
Dihya – i18n pour le module Restauration
- Messages multilingues (fr, en, ar, tzm)
"""
from django.utils.translation import gettext_lazy as _

MESSAGES = {
    'success_reservation': {
        'fr': _('Réservation enregistrée avec succès.'),
        'en': _('Reservation saved successfully.'),
        'ar': _('تم حفظ الحجز بنجاح.'),
        'tzm': _('Yettwaselmed reservation s wulhif.')
    },
    'error_permission': {
        'fr': _('Permission refusée.'),
        'en': _('Permission denied.'),
        'ar': _('تم رفض الإذن.'),
        'tzm': _('Ulac tasireft.')
    },
}
