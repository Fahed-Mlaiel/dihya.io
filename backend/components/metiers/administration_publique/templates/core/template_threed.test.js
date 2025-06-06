// template_threed.test.js – Tests unitaires JS pour template métier core
const { render3DTemplateUltra, validate3DTemplateUltra } = require('./template_threed');
describe('TemplateThreed JS (core)', () => {
  test('rendu ultra avancé', () => {
    const data = { id: 1, name: 'Cube', meta: { type: 'test' }, format: 'obj', i18n: { fr: 'Cube', en: 'Cube' } };
    const out = render3DTemplateUltra(data, { audit: 'ok', accessibility: 'ok', rgpd: 'ok' });
    expect(out).toContain('Cube');
    expect(out).toContain('RGPD: ok');
  });
  test('validation ultra avancée', () => {
    expect(validate3DTemplateUltra({ id: 1, name: 'Cube', rgpd: 'ok' })).toBeTruthy();
    expect(validate3DTemplateUltra({ id: 1 })).toBeFalsy();
  });
});
