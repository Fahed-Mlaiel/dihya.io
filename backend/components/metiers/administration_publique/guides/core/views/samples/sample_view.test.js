// Test unitaire pour sample_view.js
const { render } = require('./sample_view');
test('render fonctionne', () => {
  expect(render()).toBe('<div>Vue 3D</div>');
});
