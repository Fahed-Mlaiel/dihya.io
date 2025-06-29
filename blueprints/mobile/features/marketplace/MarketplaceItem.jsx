import React from 'react';
// Détail d’un item de la marketplace
export default function MarketplaceItem({ item }) {
  if (!item) return null;
  return (
    <div>
      <h4>{item.name}</h4>
      <p>Type : {item.type}</p>
      <p>Description : {item.description}</p>
    </div>
  );
}
