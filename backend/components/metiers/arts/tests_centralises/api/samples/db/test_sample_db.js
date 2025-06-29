// test_sample_db.js – Test ultra avancé des samples DB API Arts (centralisé)

const { sampleDbUltra } = require('../../../api/samples/db');

describe('Samples DB API Arts', () => {
  it('doit exécuter l’opération DB ultra avancée', () => {
    const result = sampleDbUltra();
    expect(result.db_status).toBe('ok');
    expect(result.records).toBeGreaterThanOrEqual(0);
  });
});
