// Tests Santé – Sécurité, RGPD, plugins, multilingue
const sante = require('./template');

describe('Santé', () => {
  it('crée un dossier avec succès', async () => {
    const res = await sante.creerDossier({ patient: { id: 1, role: 'patient' } });
    expect(res.success).toBe(true);
    expect(res.dossierId).toBeDefined();
  });

  it('exporte les données RGPD', async () => {
    const res = await sante.exportRGPD({ id: 1 });
    expect(res).toBeDefined();
  });

  it('anonymise les données RGPD', async () => {
    const res = await sante.anonymiser({ id: 1 });
    expect(res).toBeDefined();
  });

  it('enregistre un plugin', () => {
    expect(() => sante.registerPlugin(() => {})).not.toThrow();
  });
});
