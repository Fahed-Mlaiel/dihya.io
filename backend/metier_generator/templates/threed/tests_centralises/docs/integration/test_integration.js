// Tests d'intégration avancés pour la documentation threed (Node.js)
const { createApp } = require('threed/api');
const { User } = require('threed/models');
describe('App Integration', () => {
  it('should initialize the app', () => {
    const app = createApp();
    expect(app).toBeDefined();
    expect(typeof app.run).toBe('function');
  });
});
describe('User Integration', () => {
  it('should create a user for integration', () => {
    const user = new User({ username: 'integration', email: 'integration@dihya.io' });
    expect(user.username).toBe('integration');
  });
});
