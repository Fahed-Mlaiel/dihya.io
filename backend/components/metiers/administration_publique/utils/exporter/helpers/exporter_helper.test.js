// exporter_helper.test.js
// Tests unitaires JS pour exporter_helper
const { formatExportJSON } = require('./exporter_helper');

describe('formatExportJSON', () => {
  it('formate un objet en JSON compacté', () => {
    const obj = { a: 1, b: 'x' };
    expect(formatExportJSON(obj)).toBe('{"a":1,"b":"x"}');
  });
});
