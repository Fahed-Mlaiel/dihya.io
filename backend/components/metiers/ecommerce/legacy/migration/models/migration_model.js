// Modèle de données de migration legacy Ecommerce (JS)
// Ultra avancé, clé en main, conforme au cahier des charges
class MigrationLog {
  constructor(source, target, status, details = {}) {
    this.source = source;
    this.target = target;
    this.status = status;
    this.details = details;
  }
  toJSON() {
    return {
      source: this.source,
      target: this.target,
      status: this.status,
      details: this.details,
    };
  }
}
module.exports = { MigrationLog };
