// Exemple avancé d’intégration Audit JS côté Python
import { auditHello } from '../../audit/audit_helper.js';

export function runAuditSample() {
  console.log('--- Audit Python Sample (JS) ---');
  console.log(auditHello());
}

if (require.main === module) {
  runAuditSample();
}
