// services.js – Services d’audit legacy Culture (JS)
// Ce fichier doit être déplacé dans le dossier services/
const { AuditLog } = require('./models');
class AuditService {
  constructor() {
    this.logs = [];
  }
  logAction(action, user, status, details = {}) {
    const log = new AuditLog(action, user, status, details);
    this.logs.push(log);
    return log;
  }
  exportLogs() {
    return this.logs.map(log => log.toJSON());
  }
}
module.exports = { AuditService };
