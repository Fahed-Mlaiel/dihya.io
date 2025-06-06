// test_templates.js – Test de rendu des templates Jinja2 (Node.js/Jest)
const fs = require('fs');
const path = require('path');
const templatesDir = path.join(__dirname, '../templates');

describe('Templates Environnement', () => {
  it('doit contenir des fichiers .j2', () => {
    const files = fs.readdirSync(templatesDir).filter(f => f.endsWith('.j2'));
    expect(files.length).toBeGreaterThan(0);
  });
});
