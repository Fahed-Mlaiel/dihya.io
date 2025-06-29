// assets/index.js
import ReactGA from 'react-ga';
import i18n from 'i18next';
import Backend from 'i18next-http-backend';
import { initReactI18next } from 'react-i18next';
import analyticsMiddleware from './analyticsMiddleware';
import analyticsPlugin from './analyticsPlugin';

// Initialize analytics for frontend
ReactGA.initialize('YOUR_GOOGLE_ANALYTICS_TRACKING_ID');

// Initialize i18n for internationalization
i18n
  .use(Backend)
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    debug: process.env.NODE_ENV === 'development',
    interpolation: {
      escapeValue: false,
    },
  });

// Analytics middleware for backend (Node.js)
// This could be used with an Express.js application
const analyticsBackend = analyticsMiddleware({
  trackingId: 'YOUR_SERVER_SIDE_TRACKING_ID',
});

// Analytics plugin (could be used for extending functionality)
const analyticsExtPlugin = analyticsPlugin();

// Exporting the initialized modules for use in the application
export {
  ReactGA as analyticsFrontend,
  i18n as internationalization,
  analyticsBackend,
  analyticsExtPlugin,
};

// Usage example in a React component
// import { analyticsFrontend } from 'path/to/assets/index.js';
// analyticsFrontend.pageview(window.location.pathname + window.location.search);