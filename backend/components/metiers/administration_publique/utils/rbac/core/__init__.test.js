// __init__.test.js
// Test d'import du point d'entrée JS core RBAC
const entry = require('./__init__.js');
describe('Import core RBAC (__init__.js)', () => {
  it('should import rbac_core without error', () => {
    expect(entry).toBeDefined();
  });
});
