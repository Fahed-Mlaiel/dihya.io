// __init__.test.js
// Test d'import du point d'entrée JS RBAC
const entry = require('./__init__.js');
describe('Import RBAC (__init__.js)', () => {
  it('should import index without error', () => {
    expect(entry).toBeDefined();
  });
});
