// __init__.test.js
// Test d'import du point d'entrée JS samples views
const entry = require('./__init__.js');
describe('Import samples views (__init__.js)', () => {
  it('should import all samples without error', () => {
    expect(entry.admin).toBeDefined();
    expect(entry.api).toBeDefined();
    expect(entry.conformity).toBeDefined();
    expect(entry.partials).toBeDefined();
    expect(entry.public).toBeDefined();
    expect(entry.threed).toBeDefined();
  });
});
