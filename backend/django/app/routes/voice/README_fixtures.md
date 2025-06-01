# Guide des fixtures pour le module Voice

## Objectif
Ce document décrit l'utilisation des fixtures pour les tests, la démo, la conformité RGPD et la reproductibilité des scénarios métiers.

## Types de fixtures
- Fichiers audio multilingues (fr, en, ar, amazigh)
- Transcriptions associées
- Utilisateurs, permissions, logs d'audit

## Bonnes pratiques
- Fixtures anonymisées, conformes RGPD
- Assets accessibles, multilingues, robustes
- Scripts d'import/export automatisés

## Exemple d'utilisation
- python manage.py loaddata voice/fixtures.json

Voir le fichier fixtures.json et le dossier assets/ pour les exemples concrets.
