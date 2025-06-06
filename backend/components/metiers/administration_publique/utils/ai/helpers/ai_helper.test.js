// ai_helper.test.js
// Tests unitaires JS pour ai_helper
const { normalizeText } = require('./ai_helper');

describe('normalizeText', () => {
  it('normalise un texte avec accents et espaces', () => {
    expect(normalizeText('  Héllo   Wôrld  ')).toBe('Hello World');
  });
  it('gère le cas vide', () => {
    expect(normalizeText('')).toBe('');
  });
});
