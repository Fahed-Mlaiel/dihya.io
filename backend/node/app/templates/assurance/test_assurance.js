/**
 * Test unitaire et intégration – Template Assurance Dihya
 * @jest-environment node
 */
const { generateAssuranceModule, exportAssuranceData, anonymizeAssuranceData } = require('./template');

describe('Template Assurance Dihya', () => {
  it('génère un module assurance conforme', () => {
    const params = { locale: 'fr', tenant: 'org1', role: 'admin' };
    const module = generateAssuranceModule(params);
    expect(module).toHaveProperty('module', 'assurance_example');
    expect(module).toHaveProperty('locale', 'fr');
    expect(module).toHaveProperty('tenant', 'org1');
    expect(module).toHaveProperty('role', 'admin');
    expect(module).toHaveProperty('timestamp');
  });

  it('exporte les données RGPD', () => {
    const data = exportAssuranceData('user1');
    expect(data).toBeDefined();
  });

  it('anonymise les données RGPD', () => {
    const data = anonymizeAssuranceData('user1');
    expect(data).toBeDefined();
  });
});
