const { MigrationLog } = require('../../../legacy/migration/models/migration_model');

// Test ultra avancé pour model migration JS
describe('Model Migration', () => {
  it('doit valider le modèle migration nominal', () => {
    const log = new MigrationLog('src', 'tgt', 'ok', { count: 1 });
    const d = log.toJSON();
    expect(d.source).toBe('src');
    expect(d.target).toBe('tgt');
    expect(d.status).toBe('ok');
    expect(d.details).toEqual({ count: 1 });
  });
  it('doit gérer les détails vides', () => {
    const log = new MigrationLog('src', 'tgt', 'fail');
    const d = log.toJSON();
    expect(d.details).toEqual({});
  });
  it('doit gérer les edge cases', () => {
    const log = new MigrationLog('', '', '', null);
    const d = log.toJSON();
    expect(d.source).toBe('');
    expect(d.target).toBe('');
    expect(d.status).toBe('');
    expect(d.details).toEqual(null);
  });
});
