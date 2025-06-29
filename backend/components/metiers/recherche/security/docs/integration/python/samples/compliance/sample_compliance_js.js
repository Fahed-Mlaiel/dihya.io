// Exemple avancé d’intégration Compliance JS côté Python
import { complianceHello } from '../../compliance/compliance_helper.js';

export function runComplianceSample() {
  console.log('--- Compliance Python Sample (JS) ---');
  console.log(complianceHello());
}

if (require.main === module) {
  runComplianceSample();
}
