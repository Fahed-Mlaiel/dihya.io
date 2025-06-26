// Tests avancés de sécurité documentaire threed (Node.js)
const { checkPermissions, encryptData } = require('threed/security');
describe('Permission Check', () => {
  it('should allow admin to delete', () => {
    expect(checkPermissions('admin', 'delete')).toBe(true);
  });
  it('should not allow user to delete', () => {
    expect(checkPermissions('user', 'delete')).toBe(false);
  });
});
describe('Encryption', () => {
  it('should encrypt data', () => {
    const data = 'secret';
    const encrypted = encryptData(data);
    expect(encrypted).not.toBe(data);
    expect(typeof encrypted).toBe('string');
  });
});
