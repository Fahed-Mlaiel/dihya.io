import React from 'react';

/**
 * Exemple de composant React pour le plugin
 */
export default function ExampleComponent({ label = 'Plugin Component' }) {
  return <div className="plugin-component">{label}</div>;
}
