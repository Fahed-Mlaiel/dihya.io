import React from 'react';
import { useAnalytics } from './useAnalytics';

const MyComponent = () => {
  const analytics = useAnalytics();

  const trackEvent = () => {
    analytics.track('EVENT_NAME', { param: 'value' });
  };

  return (
    <div>
      <button onClick={trackEvent}>Track Event</button>
    </div>
  );
};

export default MyComponent;