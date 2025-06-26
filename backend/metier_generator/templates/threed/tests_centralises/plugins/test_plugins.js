// Tests avancés pour les plugins threed
const { loadPlugin, validatePlugin } = require('../../api/plugins');
describe('Plugins threed', () => {
  it('doit charger le plugin d’authentification et le valider', () => {
    const plugin = loadPlugin('auth');
    expect(plugin).toBeDefined();
    expect(validatePlugin(plugin)).toBe(true);
  });
  it('doit refuser un plugin non conforme', () => {
    const invalid = { name: 'Fake', hooks: [] };
    expect(validatePlugin(invalid)).toBe(false);
  });
});
