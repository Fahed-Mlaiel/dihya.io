// Contrôleur métier threed (Node.js)
const assets = [];
module.exports = {
  listAssets: (req, res) => res.json(assets),
  createAsset: (req, res) => {
    const asset = req.body;
    assets.push(asset);
    res.json(asset);
  },
  getAsset: (req, res) => {
    const asset = assets.find(a => a.id == req.params.id);
    res.json(asset || {});
  },
  deleteAsset: (req, res) => {
    const idx = assets.findIndex(a => a.id == req.params.id);
    if (idx !== -1) assets.splice(idx, 1);
    res.json({ deleted: idx !== -1 });
  }
};
