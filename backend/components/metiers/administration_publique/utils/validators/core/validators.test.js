// validators.test.js – Tests unitaires JS pour validators Threed
const validators = require('./validators');
describe('Validators Threed', () => {
  it('valide un modèle 3D correct', () => {
    expect(validators.isValidModel({ nom: 'Test', statut: 'actif' })).toBe(true);
  });
  it('rejette un modèle 3D invalide', () => {
    expect(validators.isValidModel({})).toBe(false);
  });
});
