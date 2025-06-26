// Blueprint routes API pour un asset métier (Express)
// Inclus : routes GET/POST, doc, et instructions d’extension

/**
 * Exemple de route métier avancée
 */
const express = require('express');
const router = express.Router();

// Liste des assets
router.get('/assets', (req, res) => res.json([{ id: 1, name: 'Asset 1', owner: 'Alice' }]));
// Création d’un asset
router.post('/assets', (req, res) => res.json({ message: 'Asset créé', data: req.body }));

// Instructions :
// - Ajouter d’autres routes métier ici
// - Étendre avec middlewares, hooks, etc.

module.exports = router;
