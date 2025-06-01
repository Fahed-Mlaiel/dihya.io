// Tests Science – Sécurité, RGPD, plugins, multilingue
const science = require('./template');

describe('Science', () => {
  it('crée un projet avec succès', async () => {
    const res = await science.creerProjet({ responsable: { id: 1, role: 'chercheur' } });
    expect(res.success).toBe(true);
    expect(res.projetId).toBeDefined();
  });

  it('exporte les données RGPD', async () => {
    const res = await science.exportRGPD({ id: 1 });
    expect(res).toBeDefined();
  });

  it('anonymise les données RGPD', async () => {
    const res = await science.anonymiser({ id: 1 });
    expect(res).toBeDefined();
  });

  it('enregistre un plugin', () => {
    expect(() => science.registerPlugin(() => {})).not.toThrow();
  });
});
