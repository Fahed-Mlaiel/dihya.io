// sample_sso.js
// Exemple d’intégration avancée SSO (Single Sign-On)

const { initiateSsoLogin } = require('../helpers/sso_helper');

const sso = initiateSsoLogin('google', 'https://app.dihya.io/callback');
console.log('SSO Login URL:', sso.url);
console.log('Provider:', sso.provider);
console.log('Initiated At:', sso.initiatedAt);
