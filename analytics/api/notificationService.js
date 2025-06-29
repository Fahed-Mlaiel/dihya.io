const express = require('express');
const router = express.Router();
const Notification = require('../models/notification');
const Analytics = require('analytics-module');
const { body, validationResult } = require('express-validator');
const i18n = require('i18n');

// Initialize analytics module
const analytics = new Analytics();

// Middleware to check for errors
const validate = (validations) => {
  return async (req, res, next) => {
    await Promise.all(validations.map(validation => validation.run(req)));

    const errors = validationResult(req);
    if (errors.isEmpty()) {
      return next();
    }

    res.status(400).json({ errors: errors.array() });
  };
};

// Send a notification
router.post('/send', [
  body('recipient').isEmail(),
  body('message').not().isEmpty(),
  validate
], async (req, res) => {
  try {
    const { recipient, message } = req.body;

    // Create and save the notification
    const notification = new Notification({ recipient, message });
    await notification.save();

    // Log the event in analytics
    analytics.track({
      eventType: 'notification_sent',
      eventData: { recipient, message }
    });

    res.status(200).json({ message: i18n.__('notification_sent_successfully') });
  } catch (error) {
    res.status(500).json({ message: i18n.__('internal_server_error') });
  }
});

// Analytics endpoint for notifications
router.get('/analytics', async (req, res) => {
  try {
    const stats = await analytics.getNotificationStats();
    res.status(200).json(stats);
  } catch (error) {
    res.status(500).json({ message: i18n.__('internal_server_error') });
  }
});

module.exports = router;