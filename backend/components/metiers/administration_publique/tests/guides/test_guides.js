// test_guides.js – Tests JS avancés pour la conformité des guides Threed
const fs = require('fs');
const path = require('path');

describe('Guides Threed', () => {
  const guidesDir = path.resolve(__dirname, '../guides');
  it('doit contenir les guides critiques', () => {
    const files = fs.readdirSync(guidesDir);
    expect(files).toContain('ACCESSIBILITY_GUIDE.md');
    expect(files).toContain('PLUGINS_GUIDE.md');
    expect(files).toContain('RGPD_GUIDE.md');
  });
  it('chaque guide doit avoir du contenu', () => {
    ['ACCESSIBILITY_GUIDE.md', 'PLUGINS_GUIDE.md', 'RGPD_GUIDE.md'].forEach(guide => {
      const content = fs.readFileSync(path.join(guidesDir, guide), 'utf-8');
      expect(content.length).toBeGreaterThan(10);
    });
  });
});
