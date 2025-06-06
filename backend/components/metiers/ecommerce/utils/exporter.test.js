// exporter.test.js – Tests unitaires pour exporter.js (Node.js/Jest)
const exporter = require('./exporter');
const fs = require('fs');
const path = require('path');

describe('Exporter', () => {
  const data = [
    { nom: 'A', val: 1 },
    { nom: 'B', val: 2 }
  ];
  const jsonPath = path.join(__dirname, 'test_export.json');
  const csvPath = path.join(__dirname, 'test_export.csv');

  afterAll(() => {
    [jsonPath, csvPath].forEach(f => fs.existsSync(f) && fs.unlinkSync(f));
  });

  it('exportToJSON écrit un fichier JSON', () => {
    exporter.exportToJSON(data, jsonPath);
    expect(fs.existsSync(jsonPath)).toBe(true);
    const content = JSON.parse(fs.readFileSync(jsonPath));
    expect(Array.isArray(content)).toBe(true);
  });

  it('exportToCSV écrit un fichier CSV', () => {
    exporter.exportToCSV(data, csvPath);
    expect(fs.existsSync(csvPath)).toBe(true);
    const content = fs.readFileSync(csvPath, 'utf-8');
    expect(content).toMatch('nom,val');
  });
});
