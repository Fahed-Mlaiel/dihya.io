// __init__.test.js
// Test d'import du point d'entrée JS helpers RBAC
const entry = require('./__init__.js');
describe('Import helpers RBAC (__init__.js)', () => {
  it('should import rbac_helper without error', () => {
    expect(entry).toBeDefined();
  });
});
