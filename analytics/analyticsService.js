// analyticsService.js
const axios = require('axios');
const { v4: uuidv4 } = require('uuid');

class AnalyticsService {
  constructor({ endpoint, storageService, i18nService }) {
    this.endpoint = endpoint;
    this.storageService = storageService;
    this.i18nService = i18nService;
  }

  async trackEvent(eventName, eventData, userContext) {
    try {
      const event = this._createEvent(eventName, eventData, userContext);
      await this._sendToEndpoint(event);
      await this.storageService.saveEvent(event);
    } catch (error) {
      console.error('Error tracking event:', error);
    }
  }

  _createEvent(eventName, eventData, userContext) {
    return {
      id: uuidv4(),
      name: eventName,
      data: eventData,
      user: userContext,
      timestamp: new Date().toISOString(),
    };
  }

  async _sendToEndpoint(event) {
    if (!this.endpoint) {
      throw new Error('Analytics endpoint is not configured.');
    }

    await axios.post(this.endpoint, event);
  }
}

module.exports = AnalyticsService;