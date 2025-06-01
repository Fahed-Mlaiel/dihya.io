# demo_decentralise/ — Démo Hébergement Décentralisé (IPFS, DWeb, etc.) Dihya Coding

Ce dossier contient des exemples, scripts ou documentation pour déployer et servir le backend Dihya Coding sur des infrastructures décentralisées (IPFS, DWeb, etc.).

## Objectif

- Garantir la résilience, la souveraineté et la résistance à la censure du projet.
- Permettre le déploiement du backend sur des réseaux décentralisés en complément des solutions classiques.

## Bonnes pratiques

- Documenter chaque méthode de déploiement (IPFS, DWeb, autres).
- Fournir des scripts ou exemples reproductibles.
- Ne jamais exposer de secrets ou de données sensibles dans les exemples publics.
- Tester la compatibilité et la sécurité avant toute mise en production.
- Respecter les licences open source des outils utilisés.

## Exemple de workflow

1. Générer un build statique ou un export du backend.
2. Ajouter le build à IPFS via `ipfs add`.
3. Documenter l’accès via une passerelle publique ou un nœud privé.
4. (Optionnel) Automatiser le backup sur IPFS après chaque déploiement.

## Sécurité

- Vérifier l’intégrité des fichiers publiés.
- Protéger les endpoints critiques même en environnement décentralisé.
- Prévoir une purge ou une rotation des données si nécessaire.

---

**Équipe Dihya Coding**