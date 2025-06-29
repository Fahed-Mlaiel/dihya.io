// context/AnalyticsContext.js

import React, { createContext, useContext, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

// Create a context for analytics
const AnalyticsContext = createContext();

// Provider component that wraps your app and makes an analytics object available to any child component that calls `useAnalytics()`.
export const AnalyticsProvider = ({ children }) => {
  // Function to track events
  const trackEvent = async (event, data) => {
    try {
      // Send event and data to your analytics backend
      await axios.post('/api/analytics/track', { event, data });
    } catch (error) {
      console.error('Failed to track event:', error);
    }
  };

  // Provide an analytics object with a trackEvent function to the context
  const analytics = { trackEvent };

  // Return the provider component with the analytics object
  return (
    <AnalyticsContext.Provider value={analytics}>
      {children}
    </AnalyticsContext.Provider>
  );
};

AnalyticsProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

// Hook to use analytics object
export const useAnalytics = () => {
  const context = useContext(AnalyticsContext);
  if (context === undefined) {
    throw new Error('useAnalytics must be used within a AnalyticsProvider');
  }
  return context;
};

// Export the context itself in case it's needed for advanced use cases
export default AnalyticsContext;