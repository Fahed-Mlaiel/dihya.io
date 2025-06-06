// __init__.test.js
// Test d'import du point d'entrée JS public views
const entry = require('./__init__.js');
describe('Import public views (__init__.js)', () => {
  it('should import public_views without error', () => {
    expect(entry).toBeDefined();
  });
});
