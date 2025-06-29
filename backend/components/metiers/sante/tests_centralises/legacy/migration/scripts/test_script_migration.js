const migrateLegacyData = require('../../../../../legacy/migration/scripts/migration_script');

// Test ultra avancé pour le script migration JS
describe('Script Migration', () => {
  it('doit valider le script de migration', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    migrateLegacyData('db_legacy', 'db_modern');
    expect(logs[0]).toMatch(/Migration des données de db_legacy vers db_modern/);
    expect(logs[1]).toMatch(/Migration terminée/);
    spy.mockRestore();
  });
  it('doit gérer les cas limites (source/target vides)', () => {
    const logs = [];
    const spy = jest.spyOn(console, 'log').mockImplementation(msg => logs.push(msg));
    migrateLegacyData('', '');
    expect(logs[0]).toMatch(/Migration des données de  vers /);
    expect(logs[1]).toMatch(/Migration terminée/);
    spy.mockRestore();
  });
});
