import React from 'react';
// Gestion admin de la marketplace
export default function MarketplaceAdmin({ plugins, onAdd, onRemove }) {
  return (
    <div>
      <h3>Admin Marketplace</h3>
      <button onClick={onAdd}>Ajouter un plugin</button>
      <ul>
        {plugins?.map((p, i) => <li key={i}>{p.name} <button onClick={()=>onRemove(p.id)}>Supprimer</button></li>)}
      </ul>
    </div>
  );
}
