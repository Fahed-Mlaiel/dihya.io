// analytics.config.js

const analyticsConfig = {
  // Configuration for backend analytics
  backend: {
    enabled: true,
    provider: 'GoogleAnalytics',
    config: {
      trackingId: process.env.BACKEND_ANALYTICS_TRACKING_ID,
    },
  },

  // Configuration for frontend analytics
  frontend: {
    enabled: true,
    provider: 'GoogleAnalytics',
    config: {
      trackingId: process.env.FRONTEND_ANALYTICS_TRACKING_ID,
    },
  },

  // Configuration for analytics plugins (e.g., error tracking, performance monitoring)
  plugins: [
    {
      name: 'ErrorTracking',
      enabled: true,
      provider: 'Sentry',
      config: {
        dsn: process.env.SENTRY_DSN,
      },
    },
  ],
};

module.exports = analyticsConfig;