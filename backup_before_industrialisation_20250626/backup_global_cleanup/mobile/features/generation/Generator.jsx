// Générateur No-Code avancé, intégrant l’API, l’i18n, et la marketplace de templates
import React, { useState } from 'react';
import { fetchAPI } from '../../services/apiService';
import { locales } from '../../i18n/i18n';

export default function Generator() {
  const [template, setTemplate] = useState(null);
  const [result, setResult] = useState(null);
  const handleGenerate = async () => {
    const res = await fetchAPI('/api/generate', { method: 'POST', body: JSON.stringify({ template }) });
    setResult(res);
  };
  return (
    <div>
      <h2>{locales.fr.accueil} – Générateur</h2>
      <select onChange={e=>setTemplate(e.target.value)}>
        <option value=''>Choisir un template</option>
        <option value='site'>Site Web</option>
        <option value='mobile'>App Mobile</option>
      </select>
      <button onClick={handleGenerate} disabled={!template}>Générer</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
