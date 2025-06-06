// templates_views.test.js – Tests unitaires templates views threed (JS)
const { renderTemplate } = require('./templates_views');
describe('Templates Threed', () => {
  it('rend un template HTML', () => {
    const html = renderTemplate('page', 'Hello');
    expect(html).toContain('template-page');
    expect(html).toContain('>Hello<');
  });
});
