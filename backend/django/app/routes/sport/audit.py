"""
Dihya – Audit et traçabilité pour Sport
- Logs, conformité RGPD, sécurité, multilingue
"""
import logging
from django.utils.translation import gettext_lazy as _

auditor = logging.getLogger('sport.audit')

def log_action(user, action, obj=None, extra=None):
    msg = _(f"Utilisateur {user} a effectué l'action {action} sur {obj} (extra: {extra})")
    auditor.info(msg)
    # TODO: Ajouter stockage base de données, export CSV, alertes RGPD
