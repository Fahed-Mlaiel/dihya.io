"""
Dihya Backend Assets – Audit Helper
Audit structuré, anonymisation, export logs, conformité RGPD, multilingue.
"""
import json
from datetime import datetime
from typing import List, Dict, Any

def anonymize_log_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    # Anonymisation RGPD (exemple)
    entry = entry.copy()
    if 'email' in entry:
        entry['email'] = 'anonymous@dihya.ai'
    if 'ip' in entry:
        entry['ip'] = '0.0.0.0'
    return entry

def export_audit_logs(logs: List[Dict[str, Any]], output_path: str) -> None:
    anonymized = [anonymize_log_entry(e) for e in logs]
    with open(output_path, 'w') as f:
        json.dump(anonymized, f, indent=2, ensure_ascii=False)
    print(f"[FR] Export anonymisé terminé : {output_path}\n[EN] Anonymized export done: {output_path}")

def log_action(user: str, action: str, details: Any = None) -> Dict[str, Any]:
    entry = {
        'user': user,
        'action': action,
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'details': details or {}
    }
    print(f"[AUDIT] {entry}")
    return entry
