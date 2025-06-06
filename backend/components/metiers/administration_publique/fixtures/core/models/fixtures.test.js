// fixtures.test.js - Tests ultra avancés pour fixtures.js (models)
const assert = require('assert');
const models = require('./');

describe('models/fixtures.js', () => {
  it('doit exposer un modèle 3D principal', () => {
    assert(models.sample3DModel);
    assert.strictEqual(models.sample3DModel.name, 'Cube Ultra');
    assert(models.sample3DModel.meta.validated);
  });
  it('doit exposer des assets avancés', () => {
    assert(Array.isArray(models.assets));
    assert(models.assets.length > 0);
    assert(models.assets[0].type === 'texture');
  });
  it('doit exposer des utilisateurs', () => {
    assert(Array.isArray(models.users));
    assert(models.users.some(u => u.role === 'admin'));
  });
});
