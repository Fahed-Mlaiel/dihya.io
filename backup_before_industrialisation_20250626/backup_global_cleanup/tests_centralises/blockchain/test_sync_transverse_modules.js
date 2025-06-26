const { execSync } = require('child_process');
const path = require('path');

describe('sync_transverse_modules.js', () => {
  it('synchronise bien les modules transverses manquants', () => {
    const script = path.resolve(__dirname, '../../blockchain/sync_transverse_modules.js');
    expect(() => execSync(`node ${script}`)).not.toThrow();
    const fs = require('fs');
    const modules = ['assets', 'utils', 'devops', 'docs', 'i18n'];
    modules.forEach(dir => {
      const dest = path.resolve(__dirname, '../../blockchain/', dir);
      expect(fs.existsSync(dest)).toBe(true);
    });
  });

  it('gère les cas limites : relance sans erreur si tout est déjà synchronisé', () => {
    const script = path.resolve(__dirname, '../../blockchain/sync_transverse_modules.js');
    expect(() => execSync(`node ${script}`)).not.toThrow();
  });
});
