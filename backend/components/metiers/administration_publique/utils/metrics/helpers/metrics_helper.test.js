// metrics_helper.test.js
// Tests unitaires JS pour metrics_helper
const { average } = require('./metrics_helper');

describe('average', () => {
  it('calcule la moyenne d\'un tableau', () => {
    expect(average([1, 2, 3])).toBe(2);
  });
  it('gère le cas vide', () => {
    expect(average([])).toBe(0);
  });
});
