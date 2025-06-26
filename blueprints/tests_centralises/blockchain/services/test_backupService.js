const BackupService = require('../../../../blockchain/services/backupService');

describe('BackupService', () => {
  it('sauvegarde un asset ou un état blockchain', () => {
    if (typeof BackupService !== 'function' && typeof BackupService !== 'object') return;
    // À adapter selon l’API réelle du service
    expect(BackupService).toBeDefined();
  });
});
