// permissions.js – Gestion des permissions
module.exports = {
  canEdit: (user) => user && user.permissions && user.permissions.includes('edit'),
  canView: (user) => user && user.permissions && user.permissions.includes('view'),
};
