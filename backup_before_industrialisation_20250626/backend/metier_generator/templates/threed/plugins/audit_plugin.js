// Plugin d'audit avancé
module.exports = {
  logAction: (action, user) => {
    // Logique d'audit
    console.log(`[AUDIT] ${user}: ${action}`);
  }
};
