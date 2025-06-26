// Tests avancés pour les tutoriels de documentation threed (Node.js)
const { Tutorial } = require('threed/docs');
describe('Tutorial Model', () => {
  it('should load a tutorial with correct data', () => {
    const tut = new Tutorial({ title: 'Guide Ultra', content: '...', author: 'Expert' });
    expect(tut.title).toBe('Guide Ultra');
    expect(tut.author).toBe('Expert');
    expect(tut.content.startsWith('...')).toBe(true);
  });
});
