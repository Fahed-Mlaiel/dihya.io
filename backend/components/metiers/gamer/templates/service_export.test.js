// Test JS pour le template service_export.json.j2
const fs = require('fs');
test('Le template service_export existe', () => {
  expect(fs.existsSync(__dirname + '/service_export.json.j2')).toBe(true);
});
