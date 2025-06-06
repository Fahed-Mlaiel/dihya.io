// fixtures.generator.test.js - Tests ultra avancés pour le générateur JS
const assert = require('assert');
const generator = require('./fixtures.generator');

describe('fixtures.generator.js', () => {
  it('génère un modèle 3D dynamique avancé', () => {
    const model = generator.generateModel('UltraModel', 12, 20);
    assert(model);
    assert.strictEqual(model.name, 'UltraModel');
    assert.strictEqual(model.vertices.length, 12);
    assert.strictEqual(model.faces.length, 20);
    assert(model.meta.generated);
    assert(model.meta.createdAt);
  });

  it('génère un utilisateur avancé', () => {
    const user = generator.generateUser('superadmin');
    assert(user);
    assert.strictEqual(user.role, 'superadmin');
    assert(user.name.startsWith('User_superadmin_'));
  });
});
