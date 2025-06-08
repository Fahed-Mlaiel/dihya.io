// sample_access_control.js – Exemple de contrôle d'accès clé en main

function getSampleAccessControl() {
  return {
    user: 'alice',
    resource: '/secure/data',
    action: 'read',
    result: true
  };
}

module.exports = { getSampleAccessControl };
