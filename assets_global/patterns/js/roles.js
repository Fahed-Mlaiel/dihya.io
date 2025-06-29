// roles.js – Gestion des rôles utilisateurs
module.exports = {
  isAdmin: (user) => user && user.role === 'admin',
  isUser: (user) => user && user.role === 'user',
};
