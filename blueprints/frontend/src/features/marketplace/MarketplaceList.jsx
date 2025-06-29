// Marketplace de plugins/templates, intégrant l’API et l’i18n
import React, { useEffect, useState } from 'react';
import { fetchAPI } from '../../services/apiService';
import { locales } from '../../i18n/i18n';

export default function MarketplaceList() {
  const [items, setItems] = useState([]);
  useEffect(() => {
    fetchAPI('/api/marketplace').then(setItems);
  }, []);
  return (
    <div>
      <h2>{locales.fr.accueil} – Marketplace</h2>
      <ul>
        {items.map(i => <li key={i.id}>{i.name} ({i.type})</li>)}
      </ul>
    </div>
  );
}
