/* global console */
// sample_conformity.js
// Exemple d'utilisation des conformity views (JS)
const conformity = require('../conformity/conformity_views');
console.log(conformity.checkRGPD ? conformity.checkRGPD({user: 'Alice'}) : 'Conformity check sample');
