// index.test.js – Test d’intégration du point d’entrée index.js des vues Threed
const entry = require('./index.js');
describe('Entrée index.js vues Threed', () => {
  it('expose les modules principaux', () => {
    expect(entry).toBeDefined();
    // Ajouter ici les attentes sur les exports principaux si besoin
  });
});
