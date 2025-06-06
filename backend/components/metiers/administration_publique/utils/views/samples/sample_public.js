// sample_public.js
// Exemple d'utilisation des public views (JS)
const pub = require('../public/public_views');
console.log(pub.renderPublicInfo ? pub.renderPublicInfo('Bienvenue') : 'Public info sample');
