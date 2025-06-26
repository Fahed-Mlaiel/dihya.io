// Blueprint de génération d'une API backend (Express)
module.exports = function generateBackendApi({ metier, dependances, plugins, rgpd }) {
  return `
const express = require('express');
const app = express();
// ...middlewares dynamiques (auth, rgpd, audit, etc.)

app.get('/api/${metier}', (req, res) => {
  res.json({ message: 'API ${metier} opérationnelle' });
});

module.exports = app;
`;
};
