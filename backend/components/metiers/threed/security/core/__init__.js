// __init__.js – Cœur métier sécurité 3D

const policy = require('./policy');
const crypto = require('./crypto');
const accessControl = require('./access_control');

module.exports = {
  policy,
  crypto,
  accessControl,
};
