/* global beforeEach, global */
const SecuriteLogger = require('../../../../utils/logger/core/logger');

describe('Logger Core JS – Ultra Advanced', () => {
  let logger;
  let logs;
  beforeEach(() => {
    logs = [];
    logger = new SecuriteLogger('TestModule');
    // Mock console
    global.console = {
      info: msg => logs.push({ type: 'info', msg }),
      warn: msg => logs.push({ type: 'warn', msg }),
      error: msg => logs.push({ type: 'error', msg })
    };
  });

  it('log info/warn/error/audit/fallback avec traçabilité', () => {
    logger.info('InfoMsg');
    logger.warn('WarnMsg');
    logger.error('ErrorMsg');
    logger.audit('LOGIN', 'user1', { ip: '127.0.0.1' });
    logger.fallback('FallbackMsg');
    expect(logs.find(l => l.msg.includes('[INFO][TestModule] InfoMsg'))).toBeTruthy();
    expect(logs.find(l => l.msg.includes('[WARN][TestModule] WarnMsg'))).toBeTruthy();
    expect(logs.find(l => l.msg.includes('[ERROR][TestModule] ErrorMsg'))).toBeTruthy();
    expect(logs.find(l => l.msg.includes('[AUDIT][TestModule] action=LOGIN user=user1'))).toBeTruthy();
    expect(logs.find(l => l.msg.includes('[FALLBACK][TestModule] FallbackMsg'))).toBeTruthy();
  });

  it('auditabilité: chaque log contient le nom du module', () => {
    logger.info('AuditTest');
    expect(logs[0].msg).toMatch('TestModule');
  });

  it('gère les caractères spéciaux et accessibilité', () => {
    logger.info('Élise €');
    expect(logs[0].msg).toMatch('Élise');
    expect(logs[0].msg).toMatch('€');
  });

  it('robustesse: ne plante pas sur message vide', () => {
    expect(() => logger.info('')).not.toThrow();
    expect(() => logger.warn('')).not.toThrow();
    expect(() => logger.error('')).not.toThrow();
    expect(() => logger.fallback('')).not.toThrow();
  });
});
