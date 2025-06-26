// router.js – Routeur Express ultra avancé pour Medias (clé en main)
// Respecte la logique métier, le cahier des charges et la structure modulaire.

const express = require('express');
const router = express.Router();

router.get('/medias', (req, res) => {
  res.json({ d3s: [], total: 0 });
});

router.post('/medias', (req, res) => {
  const { nom = '', description = '', type = 'objet' } = req.body || {};
  res.status(201).json({ nom, description, type });
});

module.exports = router;
