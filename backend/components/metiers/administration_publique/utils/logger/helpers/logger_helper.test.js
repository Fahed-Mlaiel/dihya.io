// logger_helper.test.js
// Tests unitaires JS pour logger_helper
const { formatLog } = require('./logger_helper');

describe('formatLog', () => {
  it('formate un message de log avec niveau et timestamp', () => {
    const result = formatLog('info', 'Test');
    expect(result).toMatch(/\[INFO\]\[.*\] Test/);
  });
});
