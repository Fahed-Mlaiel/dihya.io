// api/webhook_handler.js
const express = require('express');
const router = express.Router();
const analyticsService = require('../services/analyticsService');
const { validateWebhookRequest } = require('../middleware/validateWebhookRequest');
const { handleAnalyticsEvent } = require('../controllers/analyticsController');

// Middleware pour sécuriser et valider les requêtes entrantes
router.use(validateWebhookRequest);

// Route pour gérer les événements de webhook
router.post('/event', async (req, res) => {
  try {
    const { eventType, data } = req.body;

    // Générer des modules analytics en fonction de l'événement
    await handleAnalyticsEvent(eventType, data);

    // Réponse standard pour les webhooks
    res.status(200).send('Webhook received and processed');
  } catch (error) {
    console.error('Error handling webhook event:', error);
    res.status(500).send('Internal Server Error');
  }
});

module.exports = router;