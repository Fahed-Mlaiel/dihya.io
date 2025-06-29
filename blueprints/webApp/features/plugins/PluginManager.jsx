import React from 'react';
// Gestion des plugins installés
export default function PluginManager({ plugins, onActivate, onDeactivate }) {
  return (
    <div>
      <h3>Gestion des plugins</h3>
      <ul>
        {plugins?.map((p, i) => (
          <li key={i}>
            {p.name} - {p.active ? 'Actif' : 'Inactif'}
            <button onClick={()=>onActivate(p.id)}>Activer</button>
            <button onClick={()=>onDeactivate(p.id)}>Désactiver</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
