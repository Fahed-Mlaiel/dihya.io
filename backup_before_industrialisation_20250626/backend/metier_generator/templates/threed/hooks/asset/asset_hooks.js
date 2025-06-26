// Hooks asset threed (Node.js)
function beforeAssetCreate(data) {
  // Logique avant création d'asset
  return data;
}
function afterAssetCreate(data) {
  // Logique après création d'asset
  return data;
}
module.exports = { beforeAssetCreate, afterAssetCreate };
