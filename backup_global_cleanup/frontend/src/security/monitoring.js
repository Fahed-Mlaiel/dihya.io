// Monitoring – Logs structurés, alertes, métriques
export function logEvent(event, data) {
  // Log structuré (JSON)
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    event,
    data
  }));
}
export function sendAlert(type, message) {
  // Simule l’envoi d’une alerte (Slack, mail, webhook)
  console.warn(`[ALERT][${type}] ${message}`);
}
