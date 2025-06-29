const { formatLog } = require('../../../../utils/logger/helpers/logger_helper');

describe('Logger Helpers JS – Ultra Advanced', () => {
  it('formate un message de log avec niveau et timestamp', () => {
    const log = formatLog('info', 'Test message');
    expect(log).toMatch(/\[INFO\]/);
    expect(log).toMatch(/Test message/);
    expect(log).toMatch(/\d{4}-\d{2}-\d{2}T/); // ISO timestamp
  });

  it('gère les niveaux de log personnalisés', () => {
    const log = formatLog('warn', 'Attention!');
    expect(log).toMatch(/\[WARN\]/);
  });

  it('gère les caractères spéciaux et accessibilité', () => {
    const log = formatLog('info', 'Élise €');
    expect(log).toMatch('Élise');
    expect(log).toMatch('€');
  });

  it('auditabilité: la sortie contient toujours un timestamp', () => {
    const log = formatLog('error', 'Audit test');
    expect(log).toMatch(/\d{4}-\d{2}-\d{2}T/);
  });
});
