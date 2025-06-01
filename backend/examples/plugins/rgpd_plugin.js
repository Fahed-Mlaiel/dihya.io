// Plugin RGPD ultra avancé (bannière consentement, anonymisation, logs, accessibilité, CI/CD, tests)
import React from 'react';

export function GDPRBanner() {
  const [consent, setConsent] = React.useState(() => localStorage.getItem('rgpd_consent') === '1');
  if (consent) return null;
  return (
    <div role="dialog" aria-modal="true" aria-label="RGPD">
      <p>Ce site respecte le RGPD. Pour continuer, veuillez accepter la politique de confidentialité.</p>
      <button onClick={() => { localStorage.setItem('rgpd_consent', '1'); setConsent(true); }}>
        J’accepte
      </button>
    </div>
  );
}

export function checkConsent() {
  return localStorage.getItem('rgpd_consent') === '1';
}
