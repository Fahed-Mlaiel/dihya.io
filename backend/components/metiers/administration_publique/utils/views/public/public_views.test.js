// public_views.test.js
// Tests unitaires JS pour public_views
const { renderPublicInfo } = require('./public_views');
describe('public_views JS', () => {
  it('rend une info publique', () => {
    expect(renderPublicInfo('Bienvenue')).toMatch(/Bienvenue/);
  });
});
