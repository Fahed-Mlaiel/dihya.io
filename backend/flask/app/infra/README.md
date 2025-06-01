# infra

Documentation interne Dihya Coding.

## Objectif

Ce dossier regroupe les scripts et fichiers d’infrastructure as code (IaC) pour le déploiement, la configuration et la gestion des environnements backend Dihya Coding.

## Bonnes pratiques

- **Infrastructure as Code** : toute modification d’infra doit être versionnée ici (Terraform, Ansible, Docker, etc.).
- **Sécurité** : ne jamais stocker de secrets ou credentials en clair (utiliser des variables d’environnement ou un vault).
- **Documentation** : chaque script ou fichier doit être commenté et documenté.
- **Automatisation** : privilégier l’automatisation (CI/CD, provisioning, monitoring).
- **Auditabilité** : tracer les changements d’infrastructure via des commits explicites.

## Structure recommandée

```
infra/
├── README.md
├── terraform_example.tf      # Exemple de configuration Terraform
├── ansible_playbook.yml      # Exemple de playbook Ansible (à ajouter si besoin)
└── ...                      # Autres scripts ou fichiers IaC
```

## Exemple d’utilisation

- Déployer une base PostgreSQL avec Terraform :  
  Voir `terraform_example.tf`
- Ajouter un playbook Ansible pour la configuration serveur :  
  Voir `ansible_playbook.yml` (à créer si besoin)

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*