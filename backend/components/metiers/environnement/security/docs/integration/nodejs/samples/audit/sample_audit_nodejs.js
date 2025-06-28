// Exemple avancé d’intégration Audit Node.js
import { auditHello } from '../../audit/audit_helper.js';

export function runAuditSample() {
  console.log('--- Audit Node.js Sample ---');
  console.log(auditHello());
}

if (require.main === module) {
  runAuditSample();
}
