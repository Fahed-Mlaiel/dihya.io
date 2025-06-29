import React, { createContext } from 'react';

const AnalyticsContext = createContext();

export const AnalyticsProvider = ({ children }) => {
  // Ajoute ici la logique d'intégration analytics (trackers, events, etc.)
  const trackEvent = (event, data) => {
    // ...envoi à analyticsService
  };
  return (
    <AnalyticsContext.Provider value={{ trackEvent }}>
      {children}
    </AnalyticsContext.Provider>
  );
};

export default AnalyticsContext;
