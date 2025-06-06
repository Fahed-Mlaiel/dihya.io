// threed_views.test.js
// Tests unitaires JS pour threed_views
const { render3D } = require('./threed_views');
describe('threed_views JS', () => {
  it('rend un modèle 3D', () => {
    expect(render3D('Cube')).toMatch(/Cube/);
  });
});
