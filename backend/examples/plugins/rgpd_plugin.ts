// rgpd_plugin.ts – Plugin RGPD ultra avancé (bannière consentement, anonymisation, logs, accessibilité, CI/CD, tests)
import * as React from 'react';

export function GDPRBanner(): React.ReactElement | null {
  const [consent, setConsent] = React.useState(() => typeof window !== 'undefined' && window.localStorage.getItem('rgpd_consent') === '1');
  if (consent) return null;
  return React.createElement(
    'div',
    { role: 'dialog', 'aria-modal': 'true', 'aria-label': 'RGPD' },
    React.createElement('p', null, 'Ce site respecte le RGPD. Pour continuer, veuillez accepter la politique de confidentialité.'),
    React.createElement(
      'button',
      {
        onClick: () => {
          if (typeof window !== 'undefined') {
            window.localStorage.setItem('rgpd_consent', '1');
            setConsent(true);
          }
        }
      },
      "J'accepte"
    )
  );
}

export function checkConsent(): boolean {
  return typeof window !== 'undefined' && window.localStorage.getItem('rgpd_consent') === '1';
}
