const fallback = require('../../../../utils/exporter/fallback/fallback');

/* global beforeEach */

// Test ultra avancé fallback exporter utils (JS)
describe('Exporter Fallback Utils', () => {
  beforeEach(() => {
    fallback.fallbackExports.length = 0;
  });

  it('exportFallback ajoute un export en mémoire avec timestamp', () => {
    const data = { id: 1, user: 'Alice' };
    const result = fallback.exportFallback(data);
    expect(result).toHaveProperty('timestamp');
    expect(result.user).toBe('Alice');
    expect(fallback.fallbackExports.length).toBe(1);
  });

  it('exportFallback gère les objets vides', () => {
    const result = fallback.exportFallback({});
    expect(result).toHaveProperty('timestamp');
    expect(Object.keys(result).length).toBe(1); // seulement timestamp
  });

  it('fallbackExports conserve l’historique pour audit', () => {
    fallback.exportFallback({ id: 1 });
    fallback.exportFallback({ id: 2 });
    expect(fallback.fallbackExports.length).toBe(2);
    expect(fallback.fallbackExports[0]).toHaveProperty('timestamp');
  });

  it('exportFallback gère les caractères spéciaux et accessibilité', () => {
    const data = { user: 'Élise', euro: '€' };
    const result = fallback.exportFallback(data);
    expect(result.user).toBe('Élise');
    expect(result.euro).toBe('€');
  });

  it('auditabilité: chaque export est traçable', () => {
    fallback.exportFallback({ id: 1 });
    expect(fallback.fallbackExports[0]).toHaveProperty('timestamp');
  });
});
