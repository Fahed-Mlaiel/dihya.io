// core_metier.test.js – Test du module métier legacy/core
const { metierLegacyCore } = require('./core_legacy');
test('metierLegacyCore fonctionne', () => {
  expect(metierLegacyCore({ a: 1 })).toEqual({ a: 1, legacy: true });
  expect(() => metierLegacyCore(null)).toThrow();
});
test('metierLegacyCore RGPD anonymise', () => {
  expect(metierLegacyCore({ sensitive: 'secret' })).toEqual({ sensitive: '[anonymisé]', legacy: true, _audit: 'legacy_core_v1' });
});
test('metierLegacyCore accessibilité', () => {
  expect(metierLegacyCore({ accessible: true })).toMatchObject({ accessibility: 'checked', legacy: true, _audit: 'legacy_core_v1' });
});
test('metierLegacyCore edge case vide', () => {
  expect(metierLegacyCore({})).toEqual({ legacy: true, empty: true });
});
