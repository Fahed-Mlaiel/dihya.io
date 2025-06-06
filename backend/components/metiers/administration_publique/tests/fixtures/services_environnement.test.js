// services_environnement.test.js – Tests unitaires avancés des fixtures de services d'environnement
const services = require('./services_environnement');

describe('Services d\'environnement (fixtures avancés)', () => {
  it('La liste des services est définie, non vide et bien structurée', () => {
    expect(Array.isArray(services)).toBe(true);
    expect(services.length).toBeGreaterThan(0);
    services.forEach(service => {
      expect(service).toHaveProperty('id');
      expect(service).toHaveProperty('name');
      expect(service).toHaveProperty('status');
      expect(service).toHaveProperty('environment');
      expect(service).toHaveProperty('compliance');
      expect(service.compliance).toHaveProperty('rgpd');
      expect(service.compliance).toHaveProperty('audit');
      expect(service).toHaveProperty('lastChecked');
    });
  });

  it('Tous les services doivent avoir un statut valide', () => {
    const validStatus = ['ok', 'maintenance', 'error'];
    services.forEach(service => {
      expect(validStatus).toContain(service.status);
    });
  });
});
