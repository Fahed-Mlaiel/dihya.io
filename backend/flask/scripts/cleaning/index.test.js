// Tests avancés pour cleaning (audit, RGPD, plugins, multitenancy, monitoring, sécurité)
const { cleanData } = require('./index');
const { logAudit } = require('../../../utils/audit');
const { anonymize } = require('../../../utils/rgpd');
const { getTenantContext } = require('../../../utils/multitenant');
const { checkStatus } = require('../../../utils/monitoring');
const { checkRole } = require('../../../utils/security');
const { loadPlugin } = require('../../../plugins');

describe('cleaning module', () => {
  it('nettoie les données et loggue l’audit', () => {
    const res = cleanData('/tmp');
    expect(res).toBe(true);
    const audit = logAudit('clean', 'admin', { target: '/tmp' });
    expect(audit.op).toBe('clean');
  });
  it('respecte la RGPD (anonymisation)', () => {
    const data = { user: 'bob', secret: '123' };
    const anon = anonymize(data);
    expect(anon.secret).toBe('***');
  });
  it('supporte le multitenancy', () => {
    const ctx = getTenantContext('tenantA');
    expect(ctx.tenant).toBe('tenantA');
  });
  it('monitoring fonctionne', () => {
    const status = checkStatus();
    expect(status.status).toBe('ok');
  });
  it('vérifie la sécurité (rôle)', () => {
    expect(checkRole({ role: 'admin' }, 'clean')).toBe(true);
  });
  it('exécute un plugin de cleaning', () => {
    const plugin = loadPlugin('cleaning');
    expect(plugin.run()).toBe('ok');
  });
});
