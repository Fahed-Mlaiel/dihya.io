# Modules métiers centralisés

Ce dossier contient l’ensemble des modules métiers harmonisés de la plateforme Dihya.

## Liste des modules métiers disponibles

- a_i
- administration_publique
- agriculture
- arts
- assurance
- automobile
- banque_finance
- beaute
- blockchain
- construction
- crypto
- culture
- ecommerce
- education
- energie
- environnement
- gamer
- health
- hotellerie
- industrie
- medias
- mobile
- mode
- publicite
- recherche
- ressources_humaines
- restauration
- sante
- science
- securite
- seo
- services_personne
- social
- sport
- threed
- tourisme
- transport
- video
- voice
- voyage
- vr_ar

## Centralisation des tests

Une structure de centralisation des tests est en cours de mise en place au niveau racine du dossier `metiers`.

- Chaque module métier possède ses propres tests unitaires et d’intégration dans son sous-dossier.
- Un dossier ou script de tests centralisés (`tests_centralises/` ou équivalent) sera ajouté à la racine pour permettre l’exécution groupée et la couverture transversale.
- Les tests centralisés garantiront la cohérence inter-métiers et la non-régression globale.

## Importabilité et cohérence

Chaque sous-module métier dispose d’un fichier `__init__.py` pour garantir l’importabilité Python.
Le fichier `__init__.py` racine sera complété pour exposer les modules métiers principaux.

## Mise à jour

Ce README est généré automatiquement et doit être mis à jour à chaque ajout, suppression ou modification d’un module métier.
