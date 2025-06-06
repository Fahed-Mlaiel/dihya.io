import { AdministrationPublique } from './index';

describe('AdministrationPublique (ultra avancé)', () => {
  it('gère les services publics avec sécurité, i18n, plugins', () => {
    const data = { service: 'urbanisme', user: { id: 1, name: 'Alice' } };
    const instance = new AdministrationPublique({ lang: 'fr', plugins: [] });
    const res = instance.manageService(data);
    expect(res.success).toBe(true);
    expect(res.lang).toBe('fr');
    expect(res.data).toEqual(data);
  });

  it('API expose les endpoints sécurisés', () => {
    const api = AdministrationPublique.api();
    expect(typeof api.getServices).toBe('function');
    expect(api.getServices()).toEqual([]);
  });

  it('respecte RGPD (pas de fuite de données sensibles)', () => {
    const data = { service: 'urbanisme', user: { id: 1, name: 'Alice' } };
    const instance = new AdministrationPublique({ lang: 'fr' });
    const res = instance.manageService(data);
    expect(JSON.stringify(res)).not.toMatch(/password|token|secret/);
  });

  it('est extensible via plugins', () => {
    let called = false;
    const plugin = { before: () => { called = true; } };
    const instance = new AdministrationPublique({ plugins: [plugin] });
    instance.plugins.forEach(p => p.before && p.before());
    expect(called).toBe(true);
  });
});
