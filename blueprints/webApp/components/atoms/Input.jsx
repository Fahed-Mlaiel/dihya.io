import React from 'react';

// Composant Input avancé avec validation, gestion d’erreur et intégration formulaire
export default function Input({ value, onChange, label, error, ...props }) {
  return (
    <div className='input-group'>
      {label && <label>{label}</label>}
      <input
        value={value}
        onChange={onChange}
        {...props}
        className={error ? 'input-error' : 'input-primary'}
      />
      {error && <span className='input-error-message'>{error}</span>}
    </div>
  );
}
