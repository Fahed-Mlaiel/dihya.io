// sample_usage.js – Exemples ultra avancés pour le module metrics (clé en main)
const metrics = require('../core/metrics');
const data = require('./sample_metrics_data.json').metrics;

// Calcul de la moyenne
console.log('Moyenne:', metrics.calculerMoyenne(data));

// Calcul de la médiane
console.log('Médiane:', metrics.calculerMediane(data));

// Gestion d’erreur (données vides)
try {
  metrics.calculerMoyenne([]);
} catch (e) {
  console.error('Erreur attendue:', e.message);
}
