// index.js – Fixtures centralisées pour les tests (métier, utilisateurs, tokens, multi-langues, RGPD, audit)

module.exports = {
  user: {
    id: 1,
    username: 'testuser',
    role: 'admin',
    token: 'test-jwt-token',
    lang: 'fr',
  },
  dataArts: [
    { id: 1, name: 'Mona Lisa', type: 'peinture' },
    { id: 2, name: 'Le Penseur', type: 'sculpture' },
  ],
  dataAutomobile: [
    { id: 1, marque: 'Renault', modele: 'Clio' },
    { id: 2, marque: 'Tesla', modele: 'Model S' },
  ],
  // ...autres jeux de données métiers...
  auditLog: [],
  rgpdConsent: true,
};
