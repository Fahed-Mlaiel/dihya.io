// partials_views.test.js – Tests unitaires partials views threed (JS)
const { renderWidget } = require('./partials_views');
describe('Partials Threed', () => {
  it('rend un widget réutilisable', () => {
    const html = renderWidget('badge', 'OK');
    expect(html).toContain('widget-badge');
    expect(html).toContain('>OK<');
  });
});
