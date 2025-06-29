import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';

// Importation des fichiers de traduction
import enTranslation from './locales/en/translation.json';
import frTranslation from './locales/fr/translation.json';

// Configuration de i18next
i18n
  .use(Backend) // Charge les traductions via xhr/ajax
  .use(LanguageDetector) // Détecte la langue de l'utilisateur
  .use(initReactI18next) // Intégration avec React
  .init({
    // Ressources de traduction
    resources: {
      en: {
        translation: enTranslation,
      },
      fr: {
        translation: frTranslation,
      },
    },
    fallbackLng: 'en', // Langue de repli
    debug: false, // Désactiver en production

    // Options de détection de la langue
    detection: {
      order: ['queryString', 'cookie', 'localStorage', 'navigator', 'htmlTag'],
      caches: ['localStorage', 'cookie'],
    },

    interpolation: {
      escapeValue: false, // Pas besoin d'échapper les valeurs pour React
    },
  });

export default i18n;