// templates_mock.test.js – Tests unitaires JS pour mocks templates Threed
const mocks = require('./templates_mock');
describe('Mocks templates Threed (JS)', () => {
  test('mockRapportAudit existe', () => {
    expect(mocks.mockRapportAudit).toBeDefined();
  });
  test('mockEmailNotification existe', () => {
    expect(mocks.mockEmailNotification).toBeDefined();
  });
  test('mockAccessibiliteAudit existe', () => {
    expect(mocks.mockAccessibiliteAudit).toBeDefined();
  });
  test('mockServiceExport existe', () => {
    expect(mocks.mockServiceExport).toBeDefined();
  });
});
