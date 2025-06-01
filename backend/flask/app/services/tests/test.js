// Tests avancés pour les services (Node.js)
const { generateProject, listProjects } = require('../service');

describe('Service: generateProject', () => {
  it('should generate a web project in French', async () => {
    const res = await generateProject('web', 'fr');
    expect(res.success).toBe(true);
    expect(res.msg).toMatch(/Projet généré|Project generated/);
  });

  it('should generate an AI project in English', async () => {
    const res = await generateProject('ia', 'en');
    expect(res.success).toBe(true);
    expect(res.msg).toMatch(/Project generated/);
  });
});

describe('Service: listProjects', () => {
  it('should list projects in French', async () => {
    const res = await listProjects('fr');
    expect(Array.isArray(res)).toBe(true);
    expect(res[0].name).toBeDefined();
  });
});
// ...autres tests : plugins, audit, multitenancy, i18n, sécurité...
