// Tests avancés pour le module d'opérations (ops)
const { runOps } = require('./index');

describe('runOps – Opérations métiers avancées', () => {
  const user = { id: 'u1', role: 'admin' };
  const tenant = 'tenant1';
  const data = { secret: 'data' };
  const plugin = 'testPlugin';
  const route = '/api/ops';
  const action = 'testAction';

  it('effectue un audit complet', () => {
    const res = runOps('audit', { user, tenant, route, action });
    expect(res.success).toBe(true);
    expect(res.operation).toBe('audit');
  });

  it('gère RGPD (anonymisation, export, consentement)', () => {
    const res = runOps('rgpd', { user, data });
    expect(res.success).toBe(true);
    expect(res.details.anonymized).toBeDefined();
    expect(res.details.export).toBeDefined();
  });

  it('exécute un plugin métier', () => {
    const res = runOps('plugin', { user, plugin, action, data });
    expect(res.success).toBe(true);
    expect(res.details.pluginResult).toBeDefined();
  });

  it('gère le multitenancy', () => {
    const res = runOps('audit', { user, tenant });
    expect(res.success).toBe(true);
  });

  it('monitoring et alertes', () => {
    const res = runOps('monitoring', { user });
    expect(res.success).toBe(true);
    expect(res.details.status).toBeDefined();
  });

  it('sécurité et anti-abus', () => {
    const res = runOps('security', { user, route, action });
    expect(res.success).toBe(true);
  });

  it('reporting CI/CD', () => {
    const res = runOps('reporting', { user, tenant, route, action });
    expect(res.success).toBe(true);
    expect(res.details.report).toBeDefined();
  });

  it('refuse l’accès si rôle non autorisé', () => {
    const res = runOps('audit', { user: { id: 'u2', role: 'guest' }, route });
    expect(res.success).toBe(false);
    expect(res.error).toMatch(/Accès refusé/);
  });
});
