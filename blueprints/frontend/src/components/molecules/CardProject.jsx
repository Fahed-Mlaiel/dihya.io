import React from 'react';
// Molecule CardProject avancé
export default function CardProject({ project }) {
  return (
    <div className='card-project'>
      <h4>{project.name}</h4>
      <p>{project.description}</p>
      <span>Status : {project.status}</span>
    </div>
  );
}
