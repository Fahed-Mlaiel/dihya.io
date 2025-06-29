import React, { createContext, useContext, useReducer } from 'react';
import analyticsReducer from '../reducers/analyticsReducer';
import { initializeAnalyticsBackend } from '../api/analyticsApi';
import i18n from '../i18n'; // suppose i18n is set up for internationalization

const initialState = {
  events: [],
  user: null,
  loading: true,
  error: null,
};

const AnalyticsContext = createContext(initialState);

export const AnalyticsProvider = ({ children }) => {
  const [state, dispatch] = useReducer(analyticsReducer, initialState);

  // Initialize analytics backend on mount
  React.useEffect(() => {
    initializeAnalyticsBackend()
      .then(user => {
        dispatch({ type: 'SET_USER', payload: user });
        dispatch({ type: 'SET_LOADING', payload: false });
      })
      .catch(error => {
        dispatch({ type: 'SET_ERROR', payload: error });
        dispatch({ type: 'SET_LOADING', payload: false });
      });
  }, []);

  // Function to log events to the backend
  const logEvent = async (event) => {
    try {
      // Here you would send the event to your analytics backend
      // For example: await sendEventToBackend(event);
      dispatch({ type: 'LOG_EVENT', payload: event });
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: error });
    }
  };

  // Make sure to handle i18n and accessibility concerns in your components
  // For example, use aria labels and proper roles, provide alt text for images, etc.

  return (
    <AnalyticsContext.Provider value={{ ...state, logEvent }}>
      {children}
    </AnalyticsContext.Provider>
  );
};

export const useAnalytics = () => useContext(AnalyticsContext);