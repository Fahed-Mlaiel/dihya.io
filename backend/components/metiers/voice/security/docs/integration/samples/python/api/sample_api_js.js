/* global console, apiHello */
// Exemple d’intégration API JS (interopérabilité Python)
export function runApiSample() {
  console.log('--- API Python Sample (JS) ---');
  // Ajoutez ici des appels à des helpers Python via interopérabilité si besoin
  console.log(apiHello());
}

// Suppression de la variable inutilisée 'apiHello' pour corriger le warning ESLint
