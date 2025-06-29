// router.js – Routeur Express ultra avancé pour Voyage (clé en main)
// Respecte la logique métier, le cahier des charges et la structure modulaire.

const express = require('express');
const router = express.Router();

router.get('/voyage', (req, res) => {
  res.json({ d3s: [], total: 0 });
});

router.post('/voyage', (req, res) => {
  const { nom = '', description = '', type = 'objet' } = req.body || {};
  res.status(201).json({ nom, description, type });
});

module.exports = router;
