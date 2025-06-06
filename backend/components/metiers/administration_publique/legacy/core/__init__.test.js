const { metierLegacyCore } = require('./__init__');
test('import metierLegacyCore depuis __init__.js', () => {
  expect(metierLegacyCore).toBeDefined();
  expect(metierLegacyCore({ x: 2 })).toEqual({ x: 2, legacy: true });
});
