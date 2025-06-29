const { normalizeText } = require('../../../../utils/ai/helpers/ai_helper');

// Test ultra avancé pour helpers.js (utils/ai/helpers)
describe('AI Helpers Advanced (JS)', () => {
  it('normalise un texte avec accents et espaces', () => {
    expect(normalizeText('Élise   va à l’école')).toBe('Elise va a l’ecole');
  });

  it('retourne une chaîne vide pour une entrée vide', () => {
    expect(normalizeText('')).toBe('');
    expect(normalizeText(null)).toBe('');
    expect(normalizeText(undefined)).toBe('');
  });

  it('supprime les espaces multiples et normalise', () => {
    expect(normalizeText('  Test   avec   espaces  ')).toBe('Test avec espaces');
  });

  it('gère les caractères spéciaux et accessibilité', () => {
    expect(normalizeText('Café €')).toMatch('Cafe');
  });

  it('auditabilité: la sortie est toujours une string', () => {
    expect(typeof normalizeText('Test')).toBe('string');
  });
});
