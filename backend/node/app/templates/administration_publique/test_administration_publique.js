/**
 * Test unitaire et intégration – Template Administration Publique Dihya
 * @jest-environment node
 */
const { generateAdminPubliqueModule, exportAdminPubliqueData, anonymizeAdminPubliqueData } = require('./template');

describe('Template Administration Publique Dihya', () => {
  it('génère un module administration publique conforme', () => {
    const params = { locale: 'fr', tenant: 'org1', role: 'admin' };
    const module = generateAdminPubliqueModule(params);
    expect(module).toHaveProperty('module', 'admin_publique_example');
    expect(module).toHaveProperty('locale', 'fr');
    expect(module).toHaveProperty('tenant', 'org1');
    expect(module).toHaveProperty('role', 'admin');
    expect(module).toHaveProperty('timestamp');
  });

  it('exporte les données RGPD', () => {
    const data = exportAdminPubliqueData('user1');
    expect(data).toBeDefined();
  });

  it('anonymise les données RGPD', () => {
    const data = anonymizeAdminPubliqueData('user1');
    expect(data).toBeDefined();
  });
});
