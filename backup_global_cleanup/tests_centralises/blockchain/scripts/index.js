// index.js – Point d’entrée des tests scripts blockchain

// Ce fichier permet d’agréger et d’exécuter tous les tests du dossier via un seul import.
// Utile pour l’industrialisation, la CI/CD et l’audit global.

require('./test_deploy');
require('./test_audit');
require('./test_migrate');
require('./test_monitor');
require('./test_helpers');

// Ajoutez ici tout nouveau test métier ajouté au dossier.
