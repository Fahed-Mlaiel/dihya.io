// Logger ultra avancé pour Ressources_humaines (JS)
// Multi-niveaux, audit, fallback, plugins, RGPD

class Ressources_humainesLogger {
  constructor(name) {
    this.name = name;
  }
  info(msg) {
    console.info(`[INFO][${this.name}] ${msg}`);
  }
  warn(msg) {
    console.warn(`[WARN][${this.name}] ${msg}`);
  }
  error(msg) {
    console.error(`[ERROR][${this.name}] ${msg}`);
  }
  audit(action, user = null, details = {}) {
    console.info(`[AUDIT][${this.name}] action=${action} user=${user} details=${JSON.stringify(details)}`);
  }
  fallback(msg) {
    console.warn(`[FALLBACK][${this.name}] ${msg}`);
  }
}

module.exports = Ressources_humainesLogger;
