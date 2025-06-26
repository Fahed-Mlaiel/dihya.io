const { execSync } = require('child_process');
const path = require('path');

describe('sync_transverse_from_frontend.js', () => {
  it('synchronise bien les modules transverses autorisés', () => {
    const script = path.resolve(__dirname, '../../blockchain/sync_transverse_from_frontend.js');
    expect(() => execSync(`node ${script}`)).not.toThrow();
    const fs = require('fs');
    const allowed = ['devops', 'docs', 'assets', 'i18n', 'utils'];
    allowed.forEach(dir => {
      const dest = path.resolve(__dirname, '../../blockchain/', dir);
      expect(fs.existsSync(dest)).toBe(true);
    });
  });

  it('gère les cas limites : relance sans erreur si déjà synchronisé', () => {
    const script = path.resolve(__dirname, '../../blockchain/sync_transverse_from_frontend.js');
    expect(() => execSync(`node ${script}`)).not.toThrow();
  });
});
