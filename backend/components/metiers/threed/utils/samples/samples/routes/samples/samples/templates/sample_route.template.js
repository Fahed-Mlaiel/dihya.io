// sample_route.template.js - Template JS avancé route imbriquée
module.exports = (role = 'user') => ({
  role,
  allowed: role === 'admin' || (role === 'user')
});
