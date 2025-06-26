/* global console */

// Exemple avancé d’intégration Compliance Node.js
import { complianceHello } from '../../compliance/compliance_helper.js';

export function runComplianceSample() {
  console.log('--- Compliance Node.js Sample ---');
  console.log(complianceHello());
}

if (require.main === module) {
  runComplianceSample();
}
