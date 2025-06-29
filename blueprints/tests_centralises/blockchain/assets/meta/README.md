# Tests centralisés blockchaine

Ce dossier contient l’ensemble des tests automatisés générés pour chaque module, service, smart contract, script, config ou fonctionnalité du projet dihya.io.

## Structure
- Un dossier miroir pour chaque composant métier
- Un fichier d’index par dossier pour exécution/import global
- Des tests unitaires, intégration, sécurité, RGPD, accessibilité, auditabilité, performance

## Exécution
- JS : `npm test` ou `jest`
- Python : `pytest`
- Solidity : `forge test` ou `hardhat test`
- Shell : `bash <script>.test.sh`

## Bonnes pratiques
- Couverture exhaustive, edge cases, conformité RGPD/sécurité
- Documentation intégrée, auditabilité, maintenabilité

## Génération
Tests et index générés automatiquement par script Lead Dev.
