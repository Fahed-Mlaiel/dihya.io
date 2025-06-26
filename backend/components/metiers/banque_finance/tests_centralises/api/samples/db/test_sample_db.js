// test_sample_db.js – Test ultra avancé des samples DB API Banque_Finance (centralisé)

const { sampleDbUltra } = require('../../../api/samples/db');

describe('Samples DB API Banque_Finance', () => {
  it('doit exécuter l’opération DB ultra avancée', () => {
    const result = sampleDbUltra();
    expect(result.db_status).toBe('ok');
    expect(result.records).toBeGreaterThanOrEqual(0);
  });
});
