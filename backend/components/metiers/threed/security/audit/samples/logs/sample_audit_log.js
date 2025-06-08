// sample_audit_log.js – Exemple de log d’audit clé en main

function getSampleAuditLog() {
  return [
    '2025-06-07 10:00:00 [INFO] Audit démarré',
    '2025-06-07 10:00:01 [PERM] /core/policy.js : 600',
    '2025-06-07 10:00:02 [HASH] /core/policy.js : 8a7c...e2f',
    '2025-06-07 10:00:03 [ALERT] Accès refusé utilisateur=bob action=delete',
    '2025-06-07 10:00:04 [INFO] Audit terminé'
  ];
}

module.exports = { getSampleAuditLog };
