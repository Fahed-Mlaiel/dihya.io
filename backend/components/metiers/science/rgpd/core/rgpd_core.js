// rgpd_core.js – Fonctions cœur RGPD (JS)
/**
 * Exemple de fonction RGPD cœur métier
 */
function anonymizeData(data) {
  if (typeof data !== 'object' || data === null) throw new TypeError('Entrée invalide pour anonymizeData');
  return { ...data, anonymized: true };
}

module.exports = { anonymizeData };
