// trackEvent.js

// Importation des dépendances nécessaires
import axios from 'axios';
import i18n from './i18n'; // Supposons que i18n est configuré pour l'internationalisation

// Configuration de l'endpoint d'API pour les événements analytics
const ANALYTICS_API_ENDPOINT = '/api/analytics';

// Fonction pour envoyer les données d'événement au backend
const sendEventToServer = async (eventData) => {
  try {
    await axios.post(ANALYTICS_API_ENDPOINT, eventData);
  } catch (error) {
    console.error('Error sending analytics event:', error);
  }
};

// Fonction principale pour suivre les événements
const trackEvent = (eventName, eventProperties = {}) => {
  // Construire les données de l'événement
  const eventData = {
    name: eventName,
    properties: eventProperties,
    timestamp: new Date().toISOString(),
    language: i18n.language,
  };

  // Envoyer les données de l'événement au serveur
  sendEventToServer(eventData);
};

// Exportation de la fonction trackEvent pour utilisation dans d'autres modules
export default trackEvent;