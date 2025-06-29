import { useEffect } from 'react';
import trackEvent from '../trackEvent';

const useAnalytics = (eventName, eventProperties) => {
  useEffect(() => {
    if (eventName) {
      trackEvent(eventName, eventProperties);
    }
  }, [eventName, eventProperties]);
};

export default useAnalytics;
