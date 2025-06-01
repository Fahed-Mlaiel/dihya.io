// Tests BTP – Sécurité, RGPD, plugins, multilingue
const btp = require('./template');

describe('BTP', () => {
  it('crée un chantier avec succès', async () => {
    const res = await btp.creerChantier({ responsable: { id: 1, role: 'admin' } });
    expect(res.success).toBe(true);
    expect(res.chantierId).toBeDefined();
  });

  it('exporte les données RGPD', async () => {
    const res = await btp.exportRGPD({ id: 1 });
    expect(res).toBeDefined();
  });

  it('anonymise les données RGPD', async () => {
    const res = await btp.anonymiser({ id: 1 });
    expect(res).toBeDefined();
  });

  it('enregistre un plugin', () => {
    expect(() => btp.registerPlugin(() => {})).not.toThrow();
  });
});
