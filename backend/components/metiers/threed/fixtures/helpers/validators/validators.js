// helpers/validators.js – Helpers de validation ultra avancés (JS)
module.exports = {
  isValid3DModel: (model) => !!(model && typeof model.id === 'string' && Array.isArray(model.vertices)),
  isValidUser: (user) => !!(user && typeof user.id === 'string' && typeof user.role === 'string'),
  isFixtureAccessible: (fixture) => typeof fixture.description === 'string',
};
