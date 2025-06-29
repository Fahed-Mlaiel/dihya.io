// audit.js – Audit, logs structurés
module.exports = {
  log: (event, details) => {
    // Exemple métier : log structuré
    return `AUDIT: ${event} – ${JSON.stringify(details)}`;
  }
};
