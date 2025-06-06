// index.test.js – Test d'intégration du point d'entrée exporter JS
const exporter = require('./index');
describe('Entrée JS exporter utils threed', () => {
  it('doit exposer exportToJSON, exportToCSV, anonymize', () => {
    expect(exporter).toHaveProperty('exportToJSON');
    expect(exporter).toHaveProperty('exportToCSV');
    expect(exporter).toHaveProperty('anonymize');
  });
});
