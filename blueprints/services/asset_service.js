// Blueprint service métier Asset (Node.js)
// Exemple de service CRUD, instructions d’extension

const assets = [];

function getAllAssets() {
  return assets;
}

function createAsset(data) {
  const asset = { id: assets.length + 1, ...data };
  assets.push(asset);
  return asset;
}

// Service métier AssetService (Node.js)
class AssetService {
  create(asset) {
    return { ...asset, id: Date.now() };
  }
}

module.exports = { AssetService };
