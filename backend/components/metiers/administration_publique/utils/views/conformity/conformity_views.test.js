// conformity_views.test.js – Tests unitaires conformité views threed (JS)
const { checkRGPD, checkAccessibility } = require('./conformity_views');
describe('Conformity Threed', () => {
  it('valide la conformité RGPD', () => {
    expect(checkRGPD({ nom: 'Test' }).conform).toBe(true);
    expect(checkRGPD({ password: '123' }).conform).toBe(false);
  });
  it('valide l’accessibilité', () => {
    expect(checkAccessibility({ lang: 'fr' }).accessible).toBe(true);
    expect(checkAccessibility({} ).accessible).toBe(false);
  });
});
