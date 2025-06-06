// index.test.js – Test unitaire du point d'entrée utils (JS)
const utils = require('./index');

describe('index.js (utils)', () => {
  it('importe les modules core, i18n et rbac', () => {
    expect(utils.core).toBeDefined();
    expect(utils.i18n).toBeDefined();
    expect(utils.rbac).toBeDefined();
  });
});
