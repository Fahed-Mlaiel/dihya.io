/* global console */
// sample_partials.js
// Exemple d'utilisation des partials views (JS)
const partials = require('../partials/partials_views');
console.log(partials.renderWidget ? partials.renderWidget('badge', 'OK') : 'Widget sample');
