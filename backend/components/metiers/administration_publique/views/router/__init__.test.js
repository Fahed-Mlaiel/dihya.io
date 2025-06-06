// __init__.test.js – Test d'import du point d'entrée JS du sous-module router
const router = require('./');

test('Le module router doit être importable et être une fonction ou un objet', () => {
  expect(router).toBeDefined();
  expect(typeof router === 'function' || typeof router === 'object').toBe(true);
});
