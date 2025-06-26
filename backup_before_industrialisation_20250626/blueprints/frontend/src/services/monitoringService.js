// Service de monitoring : statistiques, alertes, santé système
/**
 * Récupère les statistiques système
 * @returns {Promise<object>} Statistiques simulées
 */
export async function getSystemStats() {
  return { uptime: 123456, users: 42, cpu: '2%', memory: '512MB' };
}

/**
 * Envoie une alerte système
 * @param {string} message
 */
export function sendAlert(message) {
  // À brancher sur un vrai système d'alerting
  console.warn('[ALERT]', message);
}
