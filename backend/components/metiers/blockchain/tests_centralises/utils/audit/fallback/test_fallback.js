/* global beforeEach */

const { auditFallback, fallbackLogs } = require('../../../../utils/audit/fallback/fallback');

// Test ultra avancé fallback audit utils (JS)
describe('Audit Fallback Utils', () => {
  beforeEach(() => {
    fallbackLogs.length = 0;
  });

  it('auditFallback ajoute un log en mémoire avec timestamp', () => {
    const log = auditFallback('LOGIN', { user: 'alice' });
    expect(log).toHaveProperty('timestamp');
    expect(log.action).toBe('LOGIN');
    expect(log.user).toBe('alice');
    expect(fallbackLogs.length).toBe(1);
  });

  it('auditFallback gère les actions vides', () => {
    const log = auditFallback('', {});
    expect(log).toHaveProperty('timestamp');
    expect(log.action).toBe('');
  });

  it('fallbackLogs conserve l’historique pour audit', () => {
    auditFallback('A1');
    auditFallback('A2');
    expect(fallbackLogs.length).toBe(2);
    expect(fallbackLogs[0]).toHaveProperty('timestamp');
  });

  it('auditFallback gère les caractères spéciaux et accessibilité', () => {
    const log = auditFallback('ÉDITION', { euro: '€' });
    expect(log.action).toBe('ÉDITION');
    expect(log.euro).toBe('€');
  });

  it('auditabilité: chaque log est traçable', () => {
    auditFallback('AUDIT');
    expect(fallbackLogs[0]).toHaveProperty('timestamp');
  });
});
