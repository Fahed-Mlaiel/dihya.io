// models.js – Modèles de logs d’audit legacy Mobile (JS)
// Ce fichier doit être déplacé dans le dossier models/
class AuditLog {
  constructor(action, user, status, details = {}, timestamp = new Date()) {
    this.action = action;
    this.user = user;
    this.status = status;
    this.details = details;
    this.timestamp = timestamp;
  }
  toJSON() {
    return {
      action: this.action,
      user: this.user,
      status: this.status,
      details: this.details,
      timestamp: this.timestamp.toISOString(),
    };
  }
}
module.exports = { AuditLog };
