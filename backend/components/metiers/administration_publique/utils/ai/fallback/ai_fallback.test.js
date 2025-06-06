// ai_fallback.test.js – Test unitaire ultra avancé fallback IA (JS)
const { aiFallback } = require('./ai_fallback');

describe('aiFallback – Fallback IA (JS)', () => {
  it('doit retourner un fallback pour une entrée non traitée', () => {
    const res = aiFallback('input-non-traite');
    expect(res.status).toBe('FALLBACK');
    expect(res.data).toBe('input-non-traite');
    expect(res.audit).toBe(true);
  });

  it('doit retourner une erreur si input vide', () => {
    const res = aiFallback();
    expect(res.status).toBe('ERROR');
  });
});
