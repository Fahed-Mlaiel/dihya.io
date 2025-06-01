"""
Exemple ultra avancé : Template métier Santé (audit, RGPD, i18n, plugins, accessibilité, CI/CD, tests)
"""
from typing import Dict, Any
from datetime import datetime
import logging

class SantePlugin:
    @staticmethod
    def anonymize(data: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in data.items() if k not in ('nom', 'prenom', 'adresse', 'email')}

    @staticmethod
    def audit(user: str, action: str, details: Any):
        logging.info(f"[AUDIT][{datetime.now()}] {user} {action} {details}")

    @staticmethod
    def process(record: Dict[str, Any], user: str, lang: str = 'fr') -> Dict[str, Any]:
        SantePlugin.audit(user, 'process', record.get('id'))
        anonymized = SantePlugin.anonymize(record)
        return {
            'anonymized': anonymized,
            'lang': lang,
            'status': 'processed',
            'timestamp': datetime.now().isoformat(),
            'tenant': record.get('tenant', 'default'),
            'role': record.get('role', 'user'),
            'fallback_ia': None,
        }

def anonymize_patient_data(patient):
    return SantePlugin.anonymize(patient)

def audit_action(user, action, details):
    SantePlugin.audit(user, action, details)

def process_medical_record(record, user, lang='fr'):
    return SantePlugin.process(record, user, lang)

if __name__ == '__main__':
    print(process_medical_record({'id': 1, 'nom': 'Dupont', 'diagnostic': 'OK'}, 'medecin1'))
