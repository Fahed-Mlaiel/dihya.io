import React from 'react';

function App() {
  // Simule un skip-link accessibilité
  // Simule un main, un titre, un sélecteur de langue, un bouton RGPD, logs, et extensibilité plugin
  const [lang, setLang] = React.useState('fr');
  const [consent, setConsent] = React.useState(() =>
    typeof window !== 'undefined' && window.localStorage.getItem('app_feature_consent') === '1'
  );
  const [logs, setLogs] = React.useState(() =>
    typeof window !== 'undefined' && window.localStorage.getItem('app_logs')
      ? JSON.parse(window.localStorage.getItem('app_logs'))
      : []
  );
  React.useEffect(() => {
    if (typeof window !== 'undefined') {
      window.localStorage.setItem('app_logs', JSON.stringify(logs));
    }
  }, [logs]);
  const handleConsent = () => {
    setConsent(true);
    if (typeof window !== 'undefined') {
      window.localStorage.setItem('app_feature_consent', '1');
    }
  };
  return (
    <>
      <a href="#main" className="skip-link">Aller au contenu</a>
      <main id="main" role="main">
        <h1>Bienvenue sur Dihya Frontend</h1>
        <label htmlFor="lang-select">Langue :</label>
        <select
          aria-label="langue"
          id="lang-select"
          value={lang}
          onChange={e => setLang(e.target.value)}
        >
          <option value="fr">Français</option>
          <option value="ar">العربية</option>
          <option value="ber">ⴰⵎⴰⵣⵉⵖ</option>
        </select>
        <div>
          {lang === 'ar' && <span>مرحبا بك في ديهيا</span>}
          {lang === 'ber' && <span>ⴰⵣⵓⵍ ⵏ ⴷⵉⵀⵢⴰ</span>}
        </div>
        <button
          data-testid="consent-required-action"
          disabled={!consent}
          onClick={handleConsent}
        >
          Action nécessitant le consentement RGPD
        </button>
        <button onClick={() => setLogs([])}>Effacer les logs</button>
        <div style={{ display: 'none' }}>{JSON.stringify(logs)}</div>
      </main>
    </>
  );
}

export default App;
