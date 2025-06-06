// __init__.test.js
// Test d'import du point d'entrée JS samples views (metiers/threed)
const entry = require('./__init__.js');
describe('Import samples views (__init__.js)', () => {
  it('should import core and helpers without error', () => {
    expect(entry.core).toBeDefined();
    expect(entry.helpers).toBeDefined();
  });
});
