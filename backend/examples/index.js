// Exemples d'utilisation de l'API backend Dihya (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, accessibilité, multitenancy, rôles, plugins, export RGPD, anonymisation, auditabilité, fallback IA)

// Exemple REST (Node.js/fetch)
async function createVRARProject() {
  const res = await fetch('/api/vr-ar/projects', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer <JWT>',
      'Content-Type': 'application/json',
      'Accept-Language': 'fr'
    },
    body: JSON.stringify({
      name: 'Projet VR Immersif',
      description: 'Expérience VR éducative multilingue',
      type: 'VR',
      owner: 'user_id'
    })
  });
  return res.json();
}

// Exemple GraphQL (Node.js/fetch)
async function createVRARProjectGraphQL() {
  const query = `mutation { createVRARProject(input: { name: "Projet AR Urbain", description: "AR pour navigation urbaine", type: "AR", owner: "user_id" }) { id name type createdAt } }`;
  const res = await fetch('/graphql/', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer <JWT>',
      'Content-Type': 'application/json',
      'Accept-Language': 'fr'
    },
    body: JSON.stringify({ query })
  });
  return res.json();
}

// Exemple RGPD : export/anonymisation
async function exportRGPDLogs() {
  const res = await fetch('/api/vr-ar/export', {
    method: 'GET',
    headers: { 'Authorization': 'Bearer <JWT>' }
  });
  return res.json();
}

// Exemple plugin dynamique
import { getPlugin, registerPlugin } from '../routes/vr_ar/plugins';
registerPlugin('demo', () => ({ result: 'plugin ok' }));
console.log(getPlugin('demo')());
