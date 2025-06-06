/* global console */
// sample_api.js
// Exemple d'utilisation des api views (JS)
const api = require('../api/api_views');
console.log(api.renderApiResponse ? api.renderApiResponse('ok') : 'API response sample');
