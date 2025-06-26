// Middleware logger API threed (Node.js) - Ultra avancé
// Journalisation structurée, corrélation, log métier, exportable
// Utilisation : app.use(require('./logger_middleware'));

const { v4: uuidv4 } = require('uuid');

function enrichLog(req, res, next) {
  req.correlationId = req.headers['x-correlation-id'] || uuidv4();
  req.startTime = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - req.startTime;
    const log = {
      correlationId: req.correlationId,
      method: req.method,
      url: req.originalUrl,
      status: res.statusCode,
      duration,
      user: req.user ? req.user.id : null,
      businessContext: req.businessContext || null
    };
    console.log('[API-LOG]', JSON.stringify(log));
  });
  next();
}

module.exports = enrichLog;

// Exemple d'intégration avancée :
// const express = require('express');
// const app = express();
// app.use(require('./logger_middleware'));
// ...
