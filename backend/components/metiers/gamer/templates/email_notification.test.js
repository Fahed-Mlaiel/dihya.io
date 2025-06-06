// Test JS pour le template email_notification.html.j2
const fs = require('fs');
test('Le template email_notification existe', () => {
  expect(fs.existsSync(__dirname + '/email_notification.html.j2')).toBe(true);
});
