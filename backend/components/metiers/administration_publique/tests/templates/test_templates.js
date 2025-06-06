// test_templates.js - Tests unitaires JS pour les templates Threed
const fs = require('fs');
const path = require('path');
const templatesDir = path.resolve(__dirname, '../templates');

describe('Templates Threed', () => {
  it('doit contenir des fichiers .j2', () => {
    const files = fs.readdirSync(templatesDir);
    expect(files.some(f => f.endsWith('.j2'))).toBe(true);
  });

  it('chaque template doit être lisible', () => {
    const files = fs.readdirSync(templatesDir).filter(f => f.endsWith('.j2'));
    files.forEach(f => {
      const content = fs.readFileSync(path.join(templatesDir, f), 'utf-8');
      expect(content.length).toBeGreaterThan(0);
    });
  });
});
