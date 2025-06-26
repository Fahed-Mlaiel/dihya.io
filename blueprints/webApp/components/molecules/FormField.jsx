import React from 'react';
// Molecule FormField avancé
export default function FormField({ label, error, children }) {
  return (
    <div className='form-field'>
      {label && <label>{label}</label>}
      {children}
      {error && <span className='form-error'>{error}</span>}
    </div>
  );
}
