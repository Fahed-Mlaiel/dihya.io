// test_db.js – Test ultra avancé de gestion DB API Health (centralisé)

const { sampleDbUltra } = require('../../../api/samples/db');

describe('DB API Health', () => {
  it('doit exécuter l’opération DB ultra avancée', () => {
    const result = sampleDbUltra();
    expect(result.db_status).toBe('ok');
    expect(result.records).toBeGreaterThanOrEqual(0);
  });
});
