// test_fallback_helper_advanced.js – Tests ultra avancés pour fallback.js (helpers/fallback)
const { loggerFallback } = require('../../../../utils/logger/fallback/fallback');
const { fallbackHelper } = require('../../../../utils/helpers/fallback/fallback');

describe('Helpers Fallback – loggerFallback (Ultra avancé)', () => {
  it('ajoute un log fallback pour auditabilité', () => {
    const log = loggerFallback('Fallback test');
    expect(log).toHaveProperty('timestamp');
    expect(log.message).toBe('Fallback test');
  });

  it('gère les logs vides', () => {
    const log = loggerFallback('');
    expect(log).toHaveProperty('timestamp');
    expect(log.message).toBe('');
  });
});

describe('Helpers Fallback – fallbackHelper (Ultra avancé)', () => {
  it('retourne le résultat de la fonction si pas d’erreur', () => {
    const fn = () => 42;
    expect(fallbackHelper(fn, 0)).toBe(42);
  });

  it('retourne la valeur par défaut si la fonction échoue', () => {
    const fn = () => { throw new Error('fail'); };
    expect(fallbackHelper(fn, 'defaut')).toBe('defaut');
  });

  it('gère les valeurs nulles et edge cases', () => {
    expect(fallbackHelper(() => null, 'x')).toBe(null);
  });

  it('auditabilité: la sortie est traçable', () => {
    expect(typeof fallbackHelper(() => 'ok', 'ko')).toBe('string');
  });
});
