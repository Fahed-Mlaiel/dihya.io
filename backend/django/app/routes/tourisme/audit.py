"""
Dihya – Audit et traçabilité pour Tourisme
- Logs, conformité RGPD, sécurité, multilingue
"""
import logging
from django.utils.translation import gettext_lazy as _

auditor = logging.getLogger('tourisme.audit')

def log_action(user, action, obj=None, extra=None):
    msg = _(f"Utilisateur {user} a effectué l'action {action} sur {obj} (extra: {extra})")
    auditor.info(msg)
    # Stockage base de données, export CSV, alertes RGPD
    try:
        from .models import AuditLog
        AuditLog.objects.create(user=user, action=action, object=str(obj), extra=str(extra))
    except Exception as e:
        print(f"[AUDIT][DB][FALLBACK] {e}")
    try:
        import csv
        with open('/tmp/tourisme_audit.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([user, action, str(obj), str(extra)])
    except Exception as e:
        print(f"[AUDIT][CSV][FALLBACK] {e}")
    # Alertes RGPD (exemple: email admin)
    # ...existing code...
