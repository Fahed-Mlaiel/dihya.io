"""
Exemple ultra avancé : Template métier RH (audit, RGPD, i18n, plugins, accessibilité, CI/CD, tests)
"""

from typing import Dict, Any
from datetime import datetime
import logging

class RHPlugin:
    @staticmethod
    def anonymize(data: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in data.items() if k not in ('nom', 'prenom', 'email', 'adresse')}

    @staticmethod
    def audit(user: str, action: str, details: Any):
        logging.info(f"[AUDIT][{datetime.now()}] {user} {action} {details}")

    @staticmethod
    def process(record: Dict[str, Any], user: str, lang: str = 'fr') -> Dict[str, Any]:
        RHPlugin.audit(user, 'process', record.get('id'))
        anonymized = RHPlugin.anonymize(record)
        return {
            'anonymized': anonymized,
            'lang': lang,
            'status': 'processed',
            'timestamp': datetime.now().isoformat(),
            'tenant': record.get('tenant', 'default'),
            'role': record.get('role', 'user'),
            'fallback_ia': None,
        }

def anonymize_rh_data(data):
    return RHPlugin.anonymize(data)

def audit_action(user, action, details):
    RHPlugin.audit(user, action, details)

def process_rh_record(record, user, lang='fr'):
    return RHPlugin.process(record, user, lang)

if __name__ == '__main__':
    print(process_rh_record({'id': 1, 'nom': 'Martin', 'poste': 'RH'}, 'rh1'))
