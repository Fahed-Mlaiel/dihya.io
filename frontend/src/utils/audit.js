// audit.js - utilitaire d’audit avancé, RGPD, logs structurés
/**
 * @file audit.js
 * @description Utilitaire d’audit, logs structurés, anonymisation, export, RGPD
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */

let logs = [];
let enabled = false;

export function enableAudit() {
  enabled = true;
}

export function logAction(action, user, details = {}) {
  if (!enabled) return;
  logs.push({
    timestamp: new Date().toISOString(),
    action,
    user: user ? { id: user.id, role: user.role, anonymized: user.isAnonymized } : null,
    details
  });
}

export function getAuditLogs() {
  return logs;
}

export function clearAuditLogs() {
  logs = [];
}

export function exportAuditLogs() {
  // RGPD: export JSON anonymisé
  return logs.map(l => ({ ...l, user: l.user ? { ...l.user, id: undefined } : null }));
}
