// exporter.test.js – Tests unitaires JS pour exporter Threed
const exporter = require('./exporter');
const fs = require('fs');
const path = require('path');

describe('Exporter Threed', () => {
  const testData = [
    { id: 1, user: 'Alice', value: 42 },
    { id: 2, user: 'Bob', value: 99 }
  ];
  const jsonPath = path.join(__dirname, 'test_export.json');
  const csvPath = path.join(__dirname, 'test_export.csv');

  afterAll(() => {
    if (fs.existsSync(jsonPath)) fs.unlinkSync(jsonPath);
    if (fs.existsSync(csvPath)) fs.unlinkSync(csvPath);
  });

  it('doit exporter en JSON', () => {
    exporter.exportToJSON(testData, jsonPath);
    const content = fs.readFileSync(jsonPath, 'utf-8');
    expect(content).toMatch('Alice');
    expect(content).toMatch('Bob');
  });

  it('doit exporter en CSV', () => {
    exporter.exportToCSV(testData, csvPath);
    const content = fs.readFileSync(csvPath, 'utf-8');
    expect(content).toMatch('Alice');
    expect(content).toMatch('Bob');
    expect(content).toMatch('id,user,value');
  });

  it('doit anonymiser les données RGPD', () => {
    const anonymized = exporter.anonymize(testData);
    expect(anonymized[0].user).toBe('anonyme');
    expect(anonymized[1].user).toBe('anonyme');
  });

  it('doit gérer le cas d’un tableau vide', () => {
    const result = exporter.exportToCSV([], csvPath);
    expect(result).toBe(csvPath);
  });
});
