# sample_audit_log.py – Exemple de log d’audit clé en main

def get_sample_audit_log():
    return [
        '2025-06-07 10:00:00 [INFO] Audit démarré',
        '2025-06-07 10:00:01 [PERM] /core/policy.py : 600',
        '2025-06-07 10:00:02 [HASH] /core/policy.py : 8a7c...e2f',
        '2025-06-07 10:00:03 [ALERT] Accès refusé utilisateur=bob action=delete',
        '2025-06-07 10:00:04 [INFO] Audit terminé'
    ]
