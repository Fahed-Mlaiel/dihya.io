// index.js - Gestion des versions de migrations (Node.js)
// Exemple de script de migration versionné, extensible, sécurisé
module.exports = {
  up: async (db) => {
    // Migration exemple : ajout table projets IA
    await db.createCollection('ai_projects');
  },
  down: async (db) => {
    await db.dropCollection('ai_projects');
  }
};
