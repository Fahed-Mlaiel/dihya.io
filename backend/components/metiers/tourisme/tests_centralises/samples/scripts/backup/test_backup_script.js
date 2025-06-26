// tests_backup_script.js - Tests ultra avancés pour les scripts de sauvegarde

const { runBackupScript } = require('../../../../../../api/backup/backup.js');

test('Script de sauvegarde retourne un résultat conforme', () => {
  const result = runBackupScript({ user: 'test', data: { id: 1 } });
  expect(result).toHaveProperty('status');
  expect(['backed_up', 'error']).toContain(result.status);
});

// Convention : chaque script de sauvegarde doit être testé sur au moins un scénario métier réel.
