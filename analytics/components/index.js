// components/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import AnalyticsProvider from './AnalyticsProvider';
import App from '../App'; // Supposons que App est le composant racine de votre application React
import analyticsBackend from '../analytics-backend'; // Module Node.js pour le backend analytics
import i18n from '../i18n'; // Module pour l'internationalisation

// Initialisation du module backend analytics
analyticsBackend.init({
  // Configuration spécifique à votre environnement et besoins
});

// Initialisation du module i18n
i18n.init({
  // Configuration spécifique à votre environnement et besoins
});

// Le composant AnalyticsProvider englobe l'application et fournit le contexte analytics
ReactDOM.render(
  <React.StrictMode>
    <AnalyticsProvider>
      <App />
    </AnalyticsProvider>
  </React.StrictMode>,
  document.getElementById('root')
);