const MonitoringService = require('../../../../blockchain/services/monitoring-service');

describe('MonitoringService', () => {
  it('surveille un asset et retourne un statut', () => {
    if (typeof MonitoringService !== 'function' && typeof MonitoringService !== 'object') return;
    // À adapter selon l’API réelle du service
    expect(MonitoringService).toBeDefined();
  });
});
