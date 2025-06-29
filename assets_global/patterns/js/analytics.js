// analytics.js – Module d’intégration analytics
module.exports = {
  trackEvent: (event, data) => {
    // Exemple métier : tracking d’événement
    return `Event '${event}' tracked with data: ${JSON.stringify(data)}`;
  }
};
