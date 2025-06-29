# Script d’analyse avancée des logs d’audit legacy Mobile
# Ultra avancé : statistiques, détection d’anomalies, RGPD, auditabilité, accessibilité
from collections import Counter
from datetime import datetime
from typing import List, Dict, Any, Optional
import copy

def anonymize_log(log: dict) -> dict:
    """Anonymise les champs sensibles pour la conformité RGPD."""
    log = copy.deepcopy(log)
    if 'user' in log:
        log['user'] = 'anonymized'
    if 'ip' in log.get('details', {}):
        log['details']['ip'] = 'x.x.x.x'
    return log

def analyse_audit_logs(logs: List[Dict[str, Any]], anonymize: bool = False) -> Dict[str, Any]:
    """
    Analyse avancée des logs d’audit :
    - Statistiques par utilisateur, action, statut
    - Détection d’anomalies (actions rares, tentatives suspectes)
    - Conformité RGPD (anonymisation possible)
    - Accessibilité (logs structurés, horodatage ISO)
    """
    if anonymize:
        logs = [anonymize_log(log) for log in logs]
    users = Counter(log['user'] for log in logs)
    actions = Counter(log['action'] for log in logs)
    status = Counter(log['status'] for log in logs)
    # Détection d’anomalies : actions rares ou suspectes
    rare_actions = [a for a, c in actions.items() if c == 1]
    suspicious = [log for log in logs if log['status'] == 'fail' or log['action'] in rare_actions]
    # Accessibilité : logs structurés, horodatage ISO
    logs_structured = [
        {
            'user': log['user'],
            'action': log['action'],
            'status': log['status'],
            'details': log.get('details', {}),
            'timestamp': log.get('timestamp', datetime.utcnow()).isoformat()
        }
        for log in logs
    ]
    return {
        'stats': {
            'users': dict(users),
            'actions': dict(actions),
            'status': dict(status),
        },
        'rare_actions': rare_actions,
        'suspicious': suspicious,
        'logs_structured': logs_structured,
        'anonymized': anonymize,
        'audit': {
            'total_logs': len(logs),
            'generated_at': datetime.utcnow().isoformat(),
        }
    }

# Hook d’extension pour plugins/metiers
def register_audit_hook(hook_fn):
    """Permet d’enregistrer un hook d’analyse métier (auditabilité, extension)."""
    global _audit_hooks
    if '_audit_hooks' not in globals():
        _audit_hooks = []
    _audit_hooks.append(hook_fn)

def run_audit_hooks(logs: List[Dict[str, Any]]):
    """Exécute tous les hooks d’audit enregistrés sur les logs."""
    for hook in globals().get('_audit_hooks', []):
        hook(logs)
