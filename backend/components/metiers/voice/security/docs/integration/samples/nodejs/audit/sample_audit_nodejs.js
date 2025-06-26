/* global console */
// Exemple d’intégration Audit Node.js ultra avancé
import { auditHello } from '../../../../nodejs/audit/audit_helper.js';

/**
 * Exécute un scénario d’intégration Audit métier Node.js
 */
export function runAuditSample() {
  console.log('--- Audit Node.js Sample (integration) ---');
  console.log(auditHello());
}
