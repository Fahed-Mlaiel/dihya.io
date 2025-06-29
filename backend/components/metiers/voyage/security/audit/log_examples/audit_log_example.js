// audit_log_example.js – Exemple de log d’audit

function getAuditLogExample() {
  return [
    '2025-06-07 10:12:01 [INFO] Audit démarré',
    '2025-06-07 10:12:02 [PERM] Fichier /core/policy.js : 600',
    '2025-06-07 10:12:03 [HASH] /core/policy.js : 8a7c...e2f',
    '2025-06-07 10:12:04 [ALERT] Accès refusé utilisateur=alice action=delete',
    '2025-06-07 10:12:05 [INFO] Audit terminé'
  ];
}

module.exports = { getAuditLogExample };
