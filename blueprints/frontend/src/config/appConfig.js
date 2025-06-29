// appConfig.js
// Configuration globale de l’application (branding, intégrations, options, etc.)

export const appConfig = {
  appName: 'Dihya.io',
  defaultLanguage: 'fr',
  supportedLanguages: ['fr', 'en', 'ar', 'de', 'es', 'it', 'kab', 'tzm', 'ru', 'pl', 'nl', 'pt', 'sv', 'no'],
  theme: 'light',
  apiBaseUrl: process.env.REACT_APP_API_URL || '/api',
  enableAnalytics: true,
  enableMonitoring: true,
  enableRGPD: true,
};
