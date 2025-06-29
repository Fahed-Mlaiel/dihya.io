import ReactGA from 'react-ga';
import { v4 as uuidv4 } from 'uuid';

const initializeAnalytics = () => {
  ReactGA.initialize('UA-XXXXXXXXX-X', {
    debug: process.env.NODE_ENV !== 'production',
    gaOptions: {
      clientId: localStorage.getItem('clientId') || uuidv4(),
    },
  });
  localStorage.setItem('clientId', ReactGA.ga(tracker => tracker.get('clientId')));
};

const trackPageView = page => {
  ReactGA.set({ page });
  ReactGA.pageview(page);
};

const trackEvent = (category, action, label) => {
  ReactGA.event({ category, action, label });
};

const setUserDetails = (userId, userProperties) => {
  ReactGA.set({ userId, ...userProperties });
};

export { initializeAnalytics, trackPageView, trackEvent, setUserDetails };