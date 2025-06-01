// Tests avancés pour RGPD (anonymisation, export, consentement, audit, plugins, multitenancy)
const { anonymizeData, exportData, recordConsent } = require('./index');
const { logAudit } = require('../../../utils/audit');
const { getTenantContext } = require('../../../utils/multitenant');
const { checkStatus } = require('../../../utils/monitoring');
const { checkRole } = require('../../../utils/security');
const { loadPlugin } = require('../../../plugins');

describe('rgpd module', () => {
  it('anonymise les données', () => {
    const data = { user: 'alice', secret: 'xyz' };
    const anon = anonymizeData(data);
    expect(anon).toBeDefined();
  });
  it('exporte les données utilisateur', () => {
    const exp = exportData('user1');
    expect(typeof exp).toBe('object');
  });
  it('enregistre le consentement', () => {
    expect(recordConsent('user1', true)).toBe(true);
  });
  it('loggue l’audit RGPD', () => {
    const audit = logAudit('rgpd', 'user1', { op: 'export' });
    expect(audit.op).toBe('rgpd');
  });
  it('supporte le multitenancy', () => {
    const ctx = getTenantContext('tenantB');
    expect(ctx.tenant).toBe('tenantB');
  });
  it('monitoring fonctionne', () => {
    const status = checkStatus();
    expect(status.status).toBe('ok');
  });
  it('vérifie la sécurité (rôle)', () => {
    expect(checkRole({ role: 'admin' }, 'rgpd')).toBe(true);
  });
  it('exécute un plugin RGPD', () => {
    const plugin = loadPlugin('rgpd');
    expect(plugin.run()).toBe('ok');
  });
});
