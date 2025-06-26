// Service métier avancé pour la gestion des assets
const assets = [];
module.exports = {
  getAllAssets: () => assets,
  createAsset: (data) => {
    const asset = { id: assets.length + 1, ...data };
    assets.push(asset);
    return asset;
  }
};
