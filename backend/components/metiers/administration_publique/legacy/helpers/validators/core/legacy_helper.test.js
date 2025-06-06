// legacy_helper.test.js – Test du helper legacy (clé en main)
const { validateLegacy } = require('./legacy_helper');

test('validateLegacy retourne true pour un objet non vide', () => {
  expect(validateLegacy({ foo: 'bar' })).toBe(true);
});

test('validateLegacy retourne false pour null ou undefined', () => {
  expect(validateLegacy(null)).toBe(false);
  expect(validateLegacy(undefined)).toBe(false);
});
