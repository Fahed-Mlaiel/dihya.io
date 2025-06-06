// __init__.test.js
// Test d'import du point d'entrée JS fallback plugins
const entry = require('./__init__.js');
describe('Import fallback plugins (__init__.js)', () => {
  it('should import plugins_fallback without error', () => {
    expect(entry).toBeDefined();
  });
});
