// Test du helper logger d’exemple (clé en main)
const { sampleLoggerHelper } = require('./sample_logger_helper');
describe('sampleLoggerHelper', () => {
  it('should log and return true', () => {
    expect(sampleLoggerHelper('clé en main')).toBe(true);
  });
});
