// Tests avancés de gestion des secrets pour la plateforme threed
describe('Secrets', () => {
  it('doit vérifier la présence du fichier .env', () => {
    const fs = require('fs');
    expect(fs.existsSync('.env')).toBe(true);
  });
  it('doit vérifier que les secrets ne sont pas commités', () => {
    const { execSync } = require('child_process');
    const output = execSync('git ls-files | grep .env', { encoding: 'utf-8' });
    expect(output).toBe('');
  });
});
