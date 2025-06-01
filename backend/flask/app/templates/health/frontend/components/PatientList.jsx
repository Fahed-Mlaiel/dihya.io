// PatientList.jsx – Template Santé Dihya (React, multilingue, accessibilité)
export default function PatientList({ patients }) {
  return (
    <section aria-label="Liste des patients">
      <h2>Patients</h2>
      <ul>
        {patients.map(p => (
          <li key={p.id}>{p.name} ({p.dob}) [{p.lang}]</li>
        ))}
      </ul>
    </section>
  );
}
