// Mock avancé pour audit métier, RGPD, sécurité, CI/CD
function logAudit(op, user, details) { return { op, user, details, ts: new Date().toISOString() }; }
function logSecurity(user, action, route) { return { user, action, route, ts: new Date().toISOString() }; }
function logOps(op, details) { return { op, details, ts: new Date().toISOString() }; }
module.exports = { logAudit, logSecurity, logOps };
