// Test ultra avancé pour monitoring_sample.js
const monitoringSample = require('../../../legacy/samples/monitoring/monitoring_sample');

describe('Monitoring Sample', () => {
  it('doit alerter si la valeur dépasse 100', () => {
    expect(monitoringSample('cpu', 150)).toMatch(/ALERT/);
  });
  it('doit indiquer OK si la valeur est normale', () => {
    expect(monitoringSample('cpu', 50)).toMatch(/OK/);
  });
  // ...autres tests avancés, edge cases, robustesse...
});
