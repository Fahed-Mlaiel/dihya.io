// Test ultra avancé de la validation d'asset (Node.js)
const validateAsset = require('../../../validations/threed_asset_validation');

describe('validateAsset', () => {
  it('valide un asset correct', () => {
    expect(validateAsset({ name: 'Ordinateur' })).toBe(true);
  });

  it('rejette un asset sans nom', () => {
    expect(() => validateAsset({})).toThrow('Le nom est requis');
  });

  // Ajoutez ici d'autres cas métier si besoin
});
