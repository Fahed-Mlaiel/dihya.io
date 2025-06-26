require('dotenv').config();
const express = require('express');

console.log('Starting server...');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    environment: process.env.NODE_ENV
  });
});

app.get('/', (req, res) => {
  res.json({
    message: '🚀 Dihya.io API Server',
    version: '1.0.0',
    environment: process.env.NODE_ENV,
    timestamp: new Date().toISOString()
  });
});

const server = app.listen(PORT, () => {
  console.log(`🚀 Serveur Dihya.io démarré sur le port ${PORT}`);
  console.log(`   Health Check: http://localhost:${PORT}/health`);
});

module.exports = app;
