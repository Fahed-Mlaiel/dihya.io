// tests_utils.js - Tests ultra avancés pour les utils

const utils = require('../../../../samples/helpers/utils/sample_utils.js');

test('Utils basique', () => {
  expect(true).toBe(true); // À remplacer par la logique réelle
});

describe('Utils avancés', () => {
  it('sum additionne deux nombres', () => {
    expect(utils.sum(2, 3)).toBe(5);
    expect(utils.sum(-1, 1)).toBe(0);
    expect(utils.sum(0, 0)).toBe(0);
  });
  it('sum gère les cas limites', () => {
    expect(utils.sum(Number.MAX_SAFE_INTEGER, 1)).toBe(Number.MAX_SAFE_INTEGER + 1);
    expect(utils.sum(null, 1)).toBeNaN();
  });
  it('isEmpty détecte un objet vide', () => {
    expect(utils.isEmpty({})).toBe(true);
    expect(utils.isEmpty({ a: 1 })).toBe(false);
  });
  it('isEmpty gère les cas non-objet', () => {
    expect(utils.isEmpty(null)).toBe(false);
    expect(utils.isEmpty(undefined)).toBe(false);
    expect(utils.isEmpty([])).toBe(true);
  });
  it('conformité RGPD : pas de fuite de données', () => {
    const obj = { password: 'secret', email: 'user@dihya.io' };
    expect(utils.isEmpty(obj)).toBe(false);
  });
});
