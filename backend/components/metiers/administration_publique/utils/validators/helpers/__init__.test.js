// __init__.test.js
// Test d'import du point d'entrée JS helpers validators
const entry = require('./__init__.js');
describe('Import helpers validators (__init__.js)', () => {
  it('should import validators_helper without error', () => {
    expect(entry).toBeDefined();
  });
});
