// rbac_engine.js – Moteur RBAC

function checkPermission(userRole, action) {
  if (userRole === 'admin') return true;
  if (userRole === 'auditor' && action === 'audit') return true;
  if (userRole === 'manager' && ['read', 'write'].includes(action)) return true;
  if (userRole === 'user' && action === 'read') return true;
  return false;
}

module.exports = { checkPermission };
