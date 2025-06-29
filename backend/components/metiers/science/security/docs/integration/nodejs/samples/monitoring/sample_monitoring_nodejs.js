// Exemple avancé d’intégration Monitoring Node.js
import { monitoringHello } from '../../monitoring/monitoring_helper.js';

export function runMonitoringSample() {
  console.log('--- Monitoring Node.js Sample ---');
  console.log(monitoringHello());
}

if (require.main === module) {
  runMonitoringSample();
}
