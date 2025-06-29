// plugins/index.js

const backendAnalytics = require('./backendAnalytics');
const frontendAnalytics = require('./frontendAnalytics');
const i18nAnalytics = require('./i18nAnalytics');
const docsAnalytics = require('./docsAnalytics');
const pluginUtils = require('./pluginUtils');

// Initialize and configure backend analytics
backendAnalytics.init({
  trackingId: process.env.BACKEND_TRACKING_ID,
  dataPrivacySettings: {
    anonymizeIP: true,
    respectDoNotTrack: true,
    GDPRCompliance: true,
  },
});

// Initialize and configure frontend analytics
frontendAnalytics.init({
  trackingId: process.env.FRONTEND_TRACKING_ID,
  dataPrivacySettings: {
    anonymizeIP: true,
    respectDoNotTrack: true,
    GDPRCompliance: true,
  },
});

// Initialize and configure i18n analytics
i18nAnalytics.init({
  trackingId: process.env.I18N_TRACKING_ID,
  dataPrivacySettings: {
    anonymizeIP: true,
    respectDoNotTrack: true,
    GDPRCompliance: true,
  },
});

// Initialize and configure documentation analytics
docsAnalytics.init({
  trackingId: process.env.DOCS_TRACKING_ID,
  dataPrivacySettings: {
    anonymizeIP: true,
    respectDoNotTrack: true,
    GDPRCompliance: true,
  },
});

// Utility function to enable or disable all analytics plugins
function toggleAnalytics(enable) {
  backendAnalytics.setEnabled(enable);
  frontendAnalytics.setEnabled(enable);
  i18nAnalytics.setEnabled(enable);
  docsAnalytics.setEnabled(enable);
}

// Export the toggle function for external control
module.exports = {
  toggleAnalytics,
};