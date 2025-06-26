// index.js
// Exporte tous les scripts et configs DevOps

module.exports = {
  DockerfileFrontend: require('./Dockerfile.frontend'),
  Backup: require('./backup.sh'),
  CI: require('./ci.yml'),
  Deploy: require('./deploy.sh'),
  Deployment: require('./deployment.yaml'),
  MainTF: require('./main.tf'),
  Maintenance: require('./maintenance.sh'),
  Restore: require('./restore.sh'),
  Seed: require('./seed.sh')
};
