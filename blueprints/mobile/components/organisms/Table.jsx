import React from 'react';
// Organism Table avancé
export default function Table({ columns, data }) {
  return (
    <table className='table'>
      <thead>
        <tr>{columns.map(col => <th key={col.key}>{col.label}</th>)}</tr>
      </thead>
      <tbody>
        {data.map((row, i) => (
          <tr key={i}>{columns.map(col => <td key={col.key}>{row[col.key]}</td>)}</tr>
        ))}
      </tbody>
    </table>
  );
}
