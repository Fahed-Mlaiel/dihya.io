// Secrets DevOps threed (Node.js)
function getSecret(key) {
  // Simule la récupération d'un secret
  return process.env[key] || null;
}
module.exports = { getSecret };
