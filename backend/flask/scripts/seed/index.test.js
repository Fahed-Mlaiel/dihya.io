// Tests avancés pour seed (audit, RGPD, plugins, multitenancy, monitoring, sécurité)
const { seedDatabase } = require('./index');
const { logAudit } = require('../../../utils/audit');
const { anonymize } = require('../../../utils/rgpd');
const { getTenantContext } = require('../../../utils/multitenant');
const { checkStatus } = require('../../../utils/monitoring');
const { checkRole } = require('../../../utils/security');
const { loadPlugin } = require('../../../plugins');

describe('seed module', () => {
  it('injecte des données de test et loggue l’audit', () => {
    const res = seedDatabase({ users: [] }, {});
    expect(res).toBe(true);
    const audit = logAudit('seed', 'admin', { table: 'users' });
    expect(audit.op).toBe('seed');
  });
  it('respecte la RGPD (anonymisation)', () => {
    const data = { user: 'bob', secret: '123' };
    const anon = anonymize(data);
    expect(anon.secret).toBe('***');
  });
  it('supporte le multitenancy', () => {
    const ctx = getTenantContext('tenantC');
    expect(ctx.tenant).toBe('tenantC');
  });
  it('monitoring fonctionne', () => {
    const status = checkStatus();
    expect(status.status).toBe('ok');
  });
  it('vérifie la sécurité (rôle)', () => {
    expect(checkRole({ role: 'admin' }, 'seed')).toBe(true);
  });
  it('exécute un plugin de seed', () => {
    const plugin = loadPlugin('seed');
    expect(plugin.run()).toBe('ok');
  });
});
