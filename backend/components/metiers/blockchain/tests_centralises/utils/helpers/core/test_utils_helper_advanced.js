// test_utils_helper_advanced.js – Tests ultra avancés pour utils_helper.js (helpers/core)
const { validateAndAudit } = require('../../../../utils/helpers/impl/advanced_impl_helper');
const utils = require('../../../../utils/helpers/core/utils_helper');

describe('Helpers Core – validateAndAudit (Ultra avancé)', () => {
  it('valide et audite des données valides (core)', () => {
    const data = { id: 10, user: 'CoreUser', email: 'core@example.com' };
    const result = validateAndAudit(data);
    expect(result.valid).toBe(true);
    expect(result.data.user).toBe('anonyme');
    expect(result.audit).toHaveProperty('timestamp');
  });

  it('rejette les données invalides (core)', () => {
    const result = validateAndAudit({});
    expect(result.valid).toBe(false);
    expect(result.data).toEqual({});
  });
});

describe('Helpers Core – utils_helper (Ultra avancé)', () => {
  it('formatDate retourne une date ISO valide', () => {
    const d = new Date('2025-06-11T12:00:00Z');
    expect(utils.formatDate(d)).toBe('2025-06-11T12:00:00.000Z');
  });

  it('isObject détecte les objets purs', () => {
    expect(utils.isObject({ a: 1 })).toBe(true);
    expect(utils.isObject([1, 2])).toBe(false);
    expect(utils.isObject(null)).toBe(false);
    expect(utils.isObject('str')).toBe(false);
  });

  it('deepClone clone profondément un objet', () => {
    const obj = { a: 1, b: { c: 2 } };
    const clone = utils.deepClone(obj);
    expect(clone).toEqual(obj);
    expect(clone).not.toBe(obj);
    clone.b.c = 99;
    expect(obj.b.c).toBe(2);
  });

  it('robustesse: deepClone gère les objets vides', () => {
    expect(utils.deepClone({})).toEqual({});
  });

  it('auditabilité: formatDate retourne toujours une string', () => {
    expect(typeof utils.formatDate(new Date())).toBe('string');
  });
});
