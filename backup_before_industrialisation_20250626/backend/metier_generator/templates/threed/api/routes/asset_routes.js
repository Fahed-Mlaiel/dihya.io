// Routes API métier threed (Node.js)
const express = require('express');
const router = express.Router();
const assetController = require('../controllers/asset_controller');
router.get('/assets', assetController.listAssets);
router.post('/assets', assetController.createAsset);
router.get('/assets/:id', assetController.getAsset);
router.delete('/assets/:id', assetController.deleteAsset);
module.exports = router;
