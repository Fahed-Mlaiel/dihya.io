// __init__.test.js
// Test d'import du point d'entrée JS core validators
const entry = require('./__init__.js');
describe('Import core validators (__init__.js)', () => {
  it('should import validators without error', () => {
    expect(entry).toBeDefined();
  });
});
