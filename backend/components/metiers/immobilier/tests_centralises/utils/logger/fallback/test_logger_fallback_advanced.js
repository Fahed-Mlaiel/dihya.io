/* global beforeEach */
const { loggerFallback, fallbackLogs } = require('../../../../utils/logger/fallback/fallback');

describe('Logger Fallback JS – Ultra Advanced', () => {
  beforeEach(() => {
    fallbackLogs.length = 0;
  });

  it('loggerFallback ajoute un log en mémoire avec timestamp', () => {
    const result = loggerFallback('Test log');
    expect(result).toHaveProperty('timestamp');
    expect(result.message).toBe('Test log');
    expect(fallbackLogs.length).toBe(1);
  });

  it('loggerFallback gère les messages vides', () => {
    const result = loggerFallback('');
    expect(result).toHaveProperty('timestamp');
    expect(result.message).toBe('');
  });

  it('fallbackLogs conserve l’historique pour audit', () => {
    loggerFallback('Log 1');
    loggerFallback('Log 2');
    expect(fallbackLogs.length).toBe(2);
    expect(fallbackLogs[0]).toHaveProperty('timestamp');
  });

  it('loggerFallback gère les caractères spéciaux et accessibilité', () => {
    const result = loggerFallback('Élise €');
    expect(result.message).toBe('Élise €');
  });

  it('auditabilité: chaque log est traçable', () => {
    loggerFallback('Audit log');
    expect(fallbackLogs[0]).toHaveProperty('timestamp');
  });
});
