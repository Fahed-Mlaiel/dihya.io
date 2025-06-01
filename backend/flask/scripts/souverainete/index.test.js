// Tests avancés pour souveraineté (audit, RGPD, plugins, multitenancy, monitoring, sécurité)
const { checkSovereignty } = require('./index');
const { logAudit } = require('../../../utils/audit');
const { anonymize } = require('../../../utils/rgpd');
const { getTenantContext } = require('../../../utils/multitenant');
const { checkStatus } = require('../../../utils/monitoring');
const { checkRole } = require('../../../utils/security');
const { loadPlugin } = require('../../../plugins');

describe('souverainete module', () => {
  it('vérifie la souveraineté et loggue l’audit', () => {
    const res = checkSovereignty({});
    expect(res).toBe(true);
    const audit = logAudit('sovereignty', 'admin', { ctx: 'test' });
    expect(audit.op).toBe('sovereignty');
  });
  it('respecte la RGPD (anonymisation)', () => {
    const data = { user: 'bob', secret: '123' };
    const anon = anonymize(data);
    expect(anon.secret).toBe('***');
  });
  it('supporte le multitenancy', () => {
    const ctx = getTenantContext('tenantD');
    expect(ctx.tenant).toBe('tenantD');
  });
  it('monitoring fonctionne', () => {
    const status = checkStatus();
    expect(status.status).toBe('ok');
  });
  it('vérifie la sécurité (rôle)', () => {
    expect(checkRole({ role: 'admin' }, 'souverainete')).toBe(true);
  });
  it('exécute un plugin souveraineté', () => {
    const plugin = loadPlugin('souverainete');
    expect(plugin.run()).toBe('ok');
  });
});
