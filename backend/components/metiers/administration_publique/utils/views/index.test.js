// index.test.js – Test d'intégration avancé du point d'entrée views JS (conformité, CI/CD, audit, multi-modules)
const views = require('./index');
describe('Entrée JS views utils threed', () => {
  it('doit exposer les helpers principaux de chaque sous-module', () => {
    expect(views).toHaveProperty('renderView');
    expect(views).toHaveProperty('renderApiResponse');
    expect(views).toHaveProperty('getAdminDashboard');
    expect(views).toHaveProperty('renderPublicInfo');
    expect(views).toHaveProperty('renderWidget');
    expect(views).toHaveProperty('checkRGPD');
    expect(views).toHaveProperty('render3D');
  });
});
