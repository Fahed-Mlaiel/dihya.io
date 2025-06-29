// monitoring_sample.js – Exemple de monitoring ultra avancé
/**
 * Simule une alerte monitoring legacy A_I
 */
function monitoringSample(metric, value) {
  // ... logique de monitoring avancée ...
  return value > 100 ? `ALERT: ${metric} dépasse le seuil!` : `OK: ${metric}`;
}

module.exports = monitoringSample;
