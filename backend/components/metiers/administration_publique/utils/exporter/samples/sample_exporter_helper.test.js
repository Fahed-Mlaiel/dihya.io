// Test du helper d’export d’exemple (JS)
const { sampleExport } = require('./sample_exporter_helper');
describe('sampleExport', () => {
  it('should log and return true', () => {
    expect(sampleExport({id: 1, name: 'Test'})).toBe(true);
  });
});
