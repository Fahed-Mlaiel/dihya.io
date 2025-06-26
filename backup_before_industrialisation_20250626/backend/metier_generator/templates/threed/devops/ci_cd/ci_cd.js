// CI/CD DevOps threed (Node.js)
function runPipeline(env) {
  console.log(`Pipeline lancé pour l'environnement ${env}`);
  return true;
}
function deployToEnv(env) {
  console.log(`Déploiement sur ${env} terminé.`);
  return true;
}
module.exports = { runPipeline, deployToEnv };
