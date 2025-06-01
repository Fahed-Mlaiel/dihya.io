// Tests Beauté – Sécurité, RGPD, plugins, multilingue
const beaute = require('./template');

describe('Beauté', () => {
  it('prend un rendez-vous avec succès', async () => {
    const res = await beaute.prendreRendezVous({ client: { id: 1, role: 'client' }, prestation: 'soin', date: '2025-06-01' });
    expect(res.success).toBe(true);
    expect(res.rdvId).toBeDefined();
  });

  it('exporte les données RGPD', async () => {
    const res = await beaute.exportRGPD({ id: 1 });
    expect(res).toBeDefined();
  });

  it('anonymise les données RGPD', async () => {
    const res = await beaute.anonymiser({ id: 1 });
    expect(res).toBeDefined();
  });

  it('enregistre un plugin', () => {
    expect(() => beaute.registerPlugin(() => {})).not.toThrow();
  });
});
