// Tests Construction – Sécurité, RGPD, plugins, multilingue
const construction = require('./template');

describe('Construction', () => {
  it('crée un projet avec succès', async () => {
    const res = await construction.creerProjet({ responsable: { id: 1, role: 'admin' } });
    expect(res.success).toBe(true);
    expect(res.projetId).toBeDefined();
  });

  it('exporte les données RGPD', async () => {
    const res = await construction.exportRGPD({ id: 1 });
    expect(res).toBeDefined();
  });

  it('anonymise les données RGPD', async () => {
    const res = await construction.anonymiser({ id: 1 });
    expect(res).toBeDefined();
  });

  it('enregistre un plugin', () => {
    expect(() => construction.registerPlugin(() => {})).not.toThrow();
  });
});
