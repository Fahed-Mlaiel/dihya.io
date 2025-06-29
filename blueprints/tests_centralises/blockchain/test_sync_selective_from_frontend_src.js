const { execSync } = require('child_process');
const path = require('path');

describe('sync_selective_from_frontend_src.js', () => {
  it('synchronise bien les dossiers autorisés depuis frontend/src', () => {
    const script = path.resolve(__dirname, '../../blockchain/sync_selective_from_frontend_src.js');
    expect(() => execSync(`node ${script}`)).not.toThrow();
    const fs = require('fs');
    const allowed = ['utils', 'assets', 'i18n'];
    allowed.forEach(dir => {
      const dest = path.resolve(__dirname, '../../blockchain/', dir);
      expect(fs.existsSync(dest)).toBe(true);
    });
  });

  it('gère les cas limites : relance sans erreur si déjà synchronisé', () => {
    const script = path.resolve(__dirname, '../../blockchain/sync_selective_from_frontend_src.js');
    expect(() => execSync(`node ${script}`)).not.toThrow();
  });
});
