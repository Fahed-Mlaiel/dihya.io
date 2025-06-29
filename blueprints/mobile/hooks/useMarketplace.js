// Hook métier pour la gestion du marketplace (listing, achat, publication)
import { useState, useEffect } from 'react';
import { getMarketplaceItems, buyItem, publishItem } from '../services/marketplaceService';

export function useMarketplace() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    getMarketplaceItems()
      .then(setItems)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  return { items, loading, error, buyItem, publishItem };
}
