// test_legacy.js – Test de compatibilité legacy pour Environnement (Node.js/Jest)
const { get_legacy_environnement } = require('../legacy/api_legacy');

describe('Legacy Environnement', () => {
  it('doit retourner une entité legacy', () => {
    const env = get_legacy_environnement(1);
    expect(env).toHaveProperty('id', 1);
    expect(env).toHaveProperty('nom');
    expect(env).toHaveProperty('statut', 'legacy');
  });
});
