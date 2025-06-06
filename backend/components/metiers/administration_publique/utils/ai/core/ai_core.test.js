// ai_core.test.js
// Tests unitaires JS pour ai_core
const { predictAI } = require('./ai_core');

describe('predictAI', () => {
  it('retourne une prédiction IA pour une entrée', () => {
    expect(predictAI('Texte')).toMatch('Prédiction pour: Texte');
  });
  it('gère le cas vide', () => {
    expect(predictAI('')).toBe('[AI-CORE] Entrée vide');
  });
});
