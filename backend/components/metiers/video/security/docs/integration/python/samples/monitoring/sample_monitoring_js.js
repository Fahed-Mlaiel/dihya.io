/* global console */
// Exemple avancé d’intégration Monitoring JS côté Python
import { monitoringHello } from '../../monitoring/monitoring_helper.js';

export function runMonitoringSample() {
  console.log('--- Monitoring Python Sample (JS) ---');
  console.log(monitoringHello());
}

if (require.main === module) {
  runMonitoringSample();
}
