// Point d'entrée global pour tous les outils DevOps du module threed
const alerting = require('./alerting');
const backup = require('./backup');
const ciCd = require('./ci_cd');
const cloud = require('./cloud');
const compliance = require('./compliance');
const infrastructure = require('./infrastructure');
const logs = require('./logs');
const monitoring = require('./monitoring');
const secrets = require('./secrets');

module.exports = {
  ...alerting,
  ...backup,
  ...ciCd,
  ...cloud,
  ...compliance,
  ...infrastructure,
  ...logs,
  ...monitoring,
  ...secrets
};
