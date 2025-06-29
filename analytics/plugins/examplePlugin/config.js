// plugins/examplePlugin/config.js

const analyticsConfig = {
  // Configuration for backend analytics
  backend: {
    enabled: true,
    provider: 'GoogleAnalytics', // or 'Mixpanel', 'Segment', etc.
    config: {
      trackingId: process.env.BACKEND_ANALYTICS_TRACKING_ID, // Use environment variable for security
    },
  },

  // Configuration for frontend analytics
  frontend: {
    enabled: true,
    provider: 'GoogleAnalytics', // or 'Mixpanel', 'Segment', etc.
    config: {
      trackingId: process.env.FRONTEND_ANALYTICS_TRACKING_ID, // Use environment variable for security
    },
  },

  // Configuration for plugin analytics
  plugins: {
    enabled: true,
    specificPluginConfig: {
      // Plugin-specific analytics configurations
    },
  },

  // Configuration for documentation analytics
  docs: {
    enabled: true,
    provider: 'GoogleAnalytics', // or another provider
    config: {
      trackingId: process.env.DOCS_ANALYTICS_TRACKING_ID, // Use environment variable for security
    },
  },

  // Internationalization (i18n) configuration for analytics
  i18n: {
    enabled: true,
    trackLocalization: true, // Track user's language preferences
  },

  // Additional configurations can be added here to make the module extensible
};

module.exports = analyticsConfig;