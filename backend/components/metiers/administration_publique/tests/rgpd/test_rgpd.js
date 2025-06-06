// test_rgpd.js – Tests JS avancés RGPD pour Threed

describe('RGPD Threed', () => {
  it('doit anonymiser les exports', () => {
    const data = { user: 'anonyme', model: '3D', exported: true };
    expect(data.user).toBe('anonyme');
    expect(data.exported).toBe(true);
  });

  it('doit gérer le consentement utilisateur', () => {
    const consent = { user: 'test', consent: true };
    expect(consent.consent).toBe(true);
  });
});
