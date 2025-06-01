// Mock sécurité (rôles, anti-abus)
function checkRole(user, op) { return user && user.role === 'admin'; }
function antiAbuse(user, route, action) { return true; }
module.exports = { checkRole, antiAbuse };
