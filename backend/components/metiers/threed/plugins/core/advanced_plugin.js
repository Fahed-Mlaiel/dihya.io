// advanced_plugin.js – Plugin avancé JS (exemple clé en main)
class AdvancedPlugin {
  constructor() {
    this.activated = false;
    this.auditTrail = [];
  }
  activate(ctx) {
    this.activated = true;
    this.auditTrail.push({ event: 'activate', ctx });
  }
  run(data) {
    if (!this.activated) throw new Error('Plugin non activé');
    this.auditTrail.push({ event: 'run', data });
    return { ...data, plugin: 'advanced', status: 'ok' };
  }
  getAuditTrail() {
    return this.auditTrail;
  }
}
module.exports = { AdvancedPlugin };
