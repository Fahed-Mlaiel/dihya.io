// fixtures_validator.js - Validation avancée des fixtures Video

module.exports = {
  isValidvideoModel: (model) => {
    return model && typeof model.id === 'string' && Array.isArray(model.vertices) && Array.isArray(model.faces);
  },
  isValidUser: (user) => {
    return user && typeof user.id === 'string' && typeof user.role === 'string';
  }
};
