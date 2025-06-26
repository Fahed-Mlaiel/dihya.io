const express = require('express');
const app = express();
const PORT = 5000;

app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date() });
});

app.listen(PORT, () => {
  console.log(`🚀 Serveur minimal sur le port ${PORT}`);
});
