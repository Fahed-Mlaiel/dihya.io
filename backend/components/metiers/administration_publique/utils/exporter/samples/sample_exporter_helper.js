// Exemple de helper d’export (JS)
function sampleExport(data) {
  console.log('[EXPORT] Données exportées:', JSON.stringify(data));
  return true;
}
module.exports = { sampleExport };
