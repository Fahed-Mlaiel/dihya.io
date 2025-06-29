// validators.js

const { isEmail, isInt, isISO8601 } = require('validator');

const validateEmail = (email) => {
  if (!isEmail(email)) {
    throw new Error('Invalid email format');
  }
};

const validateUserId = (userId) => {
  if (!isInt(userId.toString())) {
    throw new Error('User ID must be an integer');
  }
};

const validateTimestamp = (timestamp) => {
  if (!isISO8601(timestamp)) {
    throw new Error('Timestamp must be in ISO 8601 format');
  }
};

const validateAnalyticsEvent = (event) => {
  const { eventType, data } = event;
  if (typeof eventType !== 'string') {
    throw new Error('Event type must be a string');
  }

  // Extend with specific event data validations as needed
  // This is a modular approach where you can add more validations for different event types
};

module.exports = {
  validateEmail,
  validateUserId,
  validateTimestamp,
  validateAnalyticsEvent,
};