# Dihya Coding – Logs & Auditabilité Backend

## Présentation

Ce dossier contient tous les **logs d’audit** et fichiers de suivi générés par le backend Flask de Dihya Coding. La gestion des logs est essentielle pour la sécurité, la conformité RGPD, la traçabilité, la robustesse et l’auditabilité de la plateforme. Les logs permettent de suivre toutes les actions critiques : génération de projet, accès API, authentification, erreurs, modifications de données, exécution de scripts, etc.

---

## Objectifs & rôle des logs

- **Assurer la traçabilité complète des actions et accès**
- **Garantir la conformité RGPD (suppression/export sur demande)**
- **Détecter les incidents de sécurité, erreurs et anomalies**
- **Faciliter l’audit, la maintenance et le support**
- **Permettre l’analyse des usages et l’amélioration continue**
- **Sécuriser l’accès et l’intégrité des logs**

---

## Structure du dossier

```
/logs/
├── app.log                # Log principal du backend Flask (actions, erreurs, accès)
├── audit.log              # Log d’audit (modifications, accès sensibles, RGPD)
├── security.log           # Log sécurité (tentatives d’intrusion, alertes)
├── scheduler.log          # Log des tâches planifiées (jobs, backups, erreurs)
├── api.log                # Log des accès API (routes, payloads, réponses)
├── export/                # Exports RGPD des logs sur demande utilisateur
├── archive/               # Archives mensuelles/annuelles des logs
└── README.md              # (ce fichier)
```

---

## Bonnes pratiques de gestion des logs

- **Logs horodatés, structurés (JSON/YAML) et auditables**
- **Aucune donnée sensible (mot de passe, clé API, données médicales, etc.) dans les logs**
- **Rotation et archivage automatique des logs**
- **Suppression/export RGPD sur demande utilisateur**
- **Accès restreint aux logs (admin uniquement)**
- **Niveaux de logs configurables (INFO, WARNING, ERROR, AUDIT, SECURITY)**
- **Formatage et anonymisation des données sensibles**
- **Tests automatisés pour la conformité et la sécurité des logs**
- **Documentation claire sur la politique de logs**

---

## Exemples d’événements logués

- Connexion/déconnexion utilisateur, échec d’authentification
- Génération de projet, import/export de template
- Modification/suppression de données sensibles
- Exécution de scripts ou tâches planifiées
- Tentative d’accès non autorisé ou attaque détectée
- Export ou suppression RGPD des logs

---

## Sécurité & conformité RGPD

- **Suppression/export des logs sur demande utilisateur**
- **Auditabilité complète des accès et modifications**
- **Chiffrement et accès restreint aux logs sensibles**
- **Aucune donnée confidentielle dans les logs**
- **Archivage sécurisé et rotation automatique**

---

## Contribution

- Toute modification de la politique de logs doit être documentée
- Respecter la conformité RGPD et la sécurité à chaque évolution
- Proposer vos améliorations via PR ou sur la marketplace communautaire

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, ouvrez une issue ou une PR sur GitHub.*