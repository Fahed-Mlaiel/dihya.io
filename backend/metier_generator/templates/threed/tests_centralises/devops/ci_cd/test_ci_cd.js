// Tests CI/CD avancés pour la plateforme threed
const { execSync } = require('child_process');
describe('CI/CD Pipeline', () => {
  it('doit valider le build sans erreur', () => {
    const output = execSync('npm run build', { encoding: 'utf-8' });
    expect(output).toMatch(/Build completed/);
  });
  it('doit exécuter les tests unitaires', () => {
    const output = execSync('npm test', { encoding: 'utf-8' });
    expect(output).toMatch(/All tests passed/);
  });
  it('doit vérifier la présence du fichier .env.example', () => {
    const fs = require('fs');
    expect(fs.existsSync('.env.example')).toBe(true);
  });
});
