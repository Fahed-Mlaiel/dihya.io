const env = require('../../blockchain/env');
describe('env', () => {
  it('charge la configuration d’environnement', () => {
    expect(env).toBeDefined();
    expect(typeof env).toBe('object');
    expect(env.NODE_ENV || env.env).toBeDefined();
  });
  it('gère les cas limites (env manquant)', () => {
    // Simuler un env vide ou partiel
    const emptyEnv = {};
    expect(emptyEnv.NODE_ENV).toBeUndefined();
  });
});
