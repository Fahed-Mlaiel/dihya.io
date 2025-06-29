// Script JS pour générer un modèle de documentation legacy Arts
// Ultra avancé, conforme au cahier des charges
function generateModel(name, fields) {
  console.log(`# Modèle : ${name}\n`);
  fields.forEach(field => console.log(`- ${field}`));
}

if (require.main === module) {
  const name = 'Documentation technique';
  const fields = ['Titre', 'Résumé', 'Architecture', 'API', 'Sécurité', 'Déploiement', 'Maintenance'];
  generateModel(name, fields);
}
