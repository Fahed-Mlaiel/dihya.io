const { securityHelpers } = require('../../../../../../blockchain/utils/index');
describe('securityHelpers (logger)', () => {
  it('loggue une action critique', () => {
    const logs = [];
    securityHelpers.log = (msg) => logs.push(msg);
    securityHelpers.log('ALERT: Suspicious activity');
    expect(logs).toContain('ALERT: Suspicious activity');
  });
});
