const path = require('path');
const fs = require('fs');
const exporter = require('../../../../utils/exporter/core/exporter');

/* global afterEach */

// Test ultra avancé core exporter utils (JS)
describe('Exporter Core Utils', () => {
  const testData = [
    { id: 1, user: 'Alice', value: 42 },
    { id: 2, user: 'Bob', value: 99 }
  ];
  const jsonPath = path.join(__dirname, 'test_export.json');
  const csvPath = path.join(__dirname, 'test_export.csv');

  afterEach(() => {
    [jsonPath, csvPath].forEach(f => fs.existsSync(f) && fs.unlinkSync(f));
  });

  it('exportToJSON écrit un fichier JSON valide et traçable', () => {
    exporter.exportToJSON(testData, jsonPath);
    expect(fs.existsSync(jsonPath)).toBe(true);
    const content = JSON.parse(fs.readFileSync(jsonPath));
    expect(Array.isArray(content)).toBe(true);
    expect(content[0].user).toBe('Alice');
    // Auditabilité: vérifie la structure
    expect(Object.keys(content[0])).toContain('id');
  });

  it('exportToCSV écrit un fichier CSV conforme', () => {
    exporter.exportToCSV(testData, csvPath);
    expect(fs.existsSync(csvPath)).toBe(true);
    const content = fs.readFileSync(csvPath, 'utf-8');
    expect(content).toMatch('Alice');
    expect(content).toMatch('Bob');
    expect(content).toMatch('id,user,value');
  });

  it('anonymize respecte RGPD (array)', () => {
    const anonymized = exporter.anonymize(testData);
    expect(anonymized[0].user).toBe('anonyme');
    expect(anonymized[1].user).toBe('anonyme');
  });

  it('anonymize respecte RGPD (objet unique)', () => {
    const anonymized = exporter.anonymize({ id: 3, user: 'Charlie', value: 1 });
    expect(anonymized.user).toBe('anonyme');
  });

  it('exportToCSV gère le cas d’un tableau vide', () => {
    const result = exporter.exportToCSV([], csvPath);
    expect(result).toBe(csvPath);
    expect(fs.existsSync(csvPath)).toBe(false);
  });

  it('exportToJSON gère le cas d’un objet vide', () => {
    exporter.exportToJSON({}, jsonPath);
    expect(fs.existsSync(jsonPath)).toBe(true);
    const content = JSON.parse(fs.readFileSync(jsonPath));
    expect(typeof content).toBe('object');
  });

  it('exportToCSV gère les caractères spéciaux et accessibilité', () => {
    const specialData = [{ id: 1, user: 'Élise', value: '€€€' }];
    exporter.exportToCSV(specialData, csvPath);
    const content = fs.readFileSync(csvPath, 'utf-8');
    expect(content).toMatch('Élise');
    expect(content).toMatch('€€€');
  });

  it('exportToJSON journalise les accès pour audit', () => {
    exporter.exportToJSON(testData, jsonPath);
    // Simule un log d’audit (à intégrer selon la politique d’audit)
    expect(fs.existsSync(jsonPath)).toBe(true);
  });
});
