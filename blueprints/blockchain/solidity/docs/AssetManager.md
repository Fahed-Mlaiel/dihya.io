# Documentation AssetManager (Solidity)

## Description
Contrat intelligent ultra avancé pour la gestion d’actifs numériques : création, traçabilité, conformité RGPD, audit, archivage.

## Fonctions principales
- `createAsset(string name)` : Crée un nouvel actif, journalise l’event, attribue l’ownership.
- `archiveAsset(uint256 id)` : Archive un actif, vérifie l’ownership, journalise l’event.
- `getAsset(uint256 id)` : Retourne les infos d’un actif (nom, owner, date, statut).

## Sécurité & conformité
- Utilisation de SafeMath
- Contrôle d’accès (ownership)
- Events pour auditabilité
- Prêt pour audit RGPD

## Déploiement
Voir `scripts/deploy_asset_manager.js`

## Audit
Voir `scripts/audit_asset_manager.py`
