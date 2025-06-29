// hooks/index.js
import { useEffect } from 'react';

/**
 * useAnalytics est un hook personnalisé qui permet d'envoyer des données d'analytique à un backend.
 * @param {string} eventName - Le nom de l'événement à suivre.
 * @param {object} eventData - Les données associées à l'événement.
 */
export const useAnalytics = (eventName, eventData) => {
  useEffect(() => {
    // Construction de l'URL du service d'analytique
    const analyticsServiceUrl = process.env.REACT_APP_ANALYTICS_URL || 'http://localhost:5000/analytics';

    // Préparation de la requête à envoyer
    const payload = {
      eventName,
      eventData,
      timestamp: new Date().toISOString(),
    };

    // Envoi des données d'analytique au backend
    fetch(analyticsServiceUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept-Language': navigator.language,
      },
      body: JSON.stringify(payload),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Analytics data could not be sent.');
      }
      return response.json();
    })
    .then(data => {
      console.log('Analytics data sent successfully:', data);
    })
    .catch(error => {
      console.error('Error sending analytics data:', error);
    });
  }, [eventName, eventData]);
};