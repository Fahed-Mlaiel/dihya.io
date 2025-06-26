// Tests avancés d'infrastructure pour la plateforme threed
describe('Infrastructure', () => {
  it('doit vérifier la disponibilité du service Docker', () => {
    const { execSync } = require('child_process');
    const output = execSync('docker info', { encoding: 'utf-8' });
    expect(output).toMatch(/Server Version/);
  });
  it('doit vérifier la présence du fichier docker-compose.yml', () => {
    const fs = require('fs');
    expect(fs.existsSync('docker-compose.yml')).toBe(true);
  });
});
