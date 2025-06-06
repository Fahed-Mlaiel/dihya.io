// views.test.js
// Tests unitaires JS pour core views
const core = require('./views');
describe('core views JS', () => {
  it('rend une vue core', () => {
    expect(core.renderCoreView ? core.renderCoreView('Test') : 'Core view sample').toMatch(/Test/);
  });
});
