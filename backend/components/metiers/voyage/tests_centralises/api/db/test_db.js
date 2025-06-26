// test_db.js – Test ultra avancé de gestion DB API Voyage (centralisé)

const { sampleDbUltra } = require('../../../api/samples/db');

describe('DB API Voyage', () => {
  it('doit exécuter l’opération DB ultra avancée', () => {
    const result = sampleDbUltra();
    expect(result.db_status).toBe('ok');
    expect(result.records).toBeGreaterThanOrEqual(0);
  });
});
