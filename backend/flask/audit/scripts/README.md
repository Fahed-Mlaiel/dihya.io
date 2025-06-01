# audit/scripts — Scripts d’audit et de maintenance des logs Dihya Coding

Ce dossier contient les scripts utilitaires pour la gestion, la rotation et la conformité des logs d’audit du backend Dihya Coding.

## Objectif

- Automatiser la rotation, l’archivage et la purge des logs d’audit pour conformité RGPD et audit externe.
- Faciliter la maintenance et la traçabilité des actions sensibles.
- Prévenir la saturation disque et garantir la souveraineté des données d’audit.

## Bonnes pratiques

- Restreindre l’accès à ces scripts aux administrateurs ou responsables conformité.
- Ne jamais supprimer de logs sans archivage préalable.
- Logger chaque opération critique (rotation, purge, export).
- Prévoir une politique de rétention adaptée (ex : suppression des archives trop anciennes).
- Documenter chaque script (usage, arguments, exemples).

## Scripts fournis

- `rotate_audit_logs.py` : Archive le log d’audit courant avec timestamp et crée un nouveau fichier vide. Gère la rétention automatique.
- `purge_rgpd.py` : (À compléter) Script de purge sélective pour répondre aux demandes RGPD (suppression ciblée).

## Exemple d’utilisation

```bash
python rotate_audit_logs.py --logfile ../audit.log --archive-dir ../archives --max-archives 12