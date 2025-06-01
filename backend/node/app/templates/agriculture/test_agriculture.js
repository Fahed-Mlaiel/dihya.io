/**
 * Test unitaire et intégration – Template Agriculture Dihya
 * @jest-environment node
 */
const { generateAgricultureModule, exportAgricultureData, anonymizeAgricultureData } = require('./template');

describe('Template Agriculture Dihya', () => {
  it('génère un module agriculture conforme', () => {
    const params = { locale: 'fr', tenant: 'org1', role: 'admin' };
    const module = generateAgricultureModule(params);
    expect(module).toHaveProperty('module', 'agriculture_example');
    expect(module).toHaveProperty('locale', 'fr');
    expect(module).toHaveProperty('tenant', 'org1');
    expect(module).toHaveProperty('role', 'admin');
    expect(module).toHaveProperty('timestamp');
  });

  it('exporte les données RGPD', () => {
    const data = exportAgricultureData('user1');
    expect(data).toBeDefined();
  });

  it('anonymise les données RGPD', () => {
    const data = anonymizeAgricultureData('user1');
    expect(data).toBeDefined();
  });
});
