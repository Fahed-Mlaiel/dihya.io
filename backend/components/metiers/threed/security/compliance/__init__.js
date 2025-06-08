// __init__.js – Compliance sécurité 3D

const anonymisation = require('./anonymisation');
const purge = require('./purge');
const checklists = require('./checklists');
const policies = require('./policies');

module.exports = {
  anonymisation,
  purge,
  checklists,
  policies,
};
