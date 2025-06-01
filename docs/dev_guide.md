# Guide Développeur – Dihya Coding

Ce guide explique comment contribuer, développer, tester et étendre la plateforme Dihya Coding, conformément au cahier des charges : sécurité, modularité, multistack, multilingue, bonnes pratiques et extensibilité.

---

## Prérequis

- **Git** (gestion de version)
- **Python 3.11+** (pour backend Flask)
- **Node.js 20+** (pour backend Node.js et frontend React)
- **Docker** (pour conteneurisation)
- **Terraform, kubectl** (pour DevOps)
- **Solidity, Hardhat/Truffle** (pour blockchain)
- **Un éditeur moderne** (VS Code recommandé)

---

## Installation du projet

1. **Cloner le dépôt**
   ```bash
   git clone <url_du_repo>
   cd Dihya
   ```

2. **Configurer les variables d’environnement**
   - Copier les fichiers `.env` modèles dans chaque stack (`backend/flask/.env`, `backend/node/.env`, etc.)
   - Adapter les secrets et paramètres selon votre environnement

3. **Installer les dépendances**
   - **Backend Flask** :  
     ```bash
     cd Dihya/backend/flask
     pip install -r requirements.txt
     ```
   - **Backend Node.js** :  
     ```bash
     cd Dihya/backend/node
     npm install
     ```
   - **Frontend React** :  
     ```bash
     cd Dihya/frontend
     npm install
     ```

---

## Lancement local

- **Backend Flask** :  
  ```bash
  python run.py
  ```
- **Backend Node.js** :  
  ```bash
  npm start
  ```
- **Frontend React** :  
  ```bash
  npm start
  ```

---

## Structure du projet

Voir le fichier `inventaire_projet.txt` pour la structure complète.

- **backend/flask/** : API Flask, sécurité, tests, i18n, SEO, etc.
- **backend/node/** : API Node.js, sécurité, tests, i18n, SEO, etc.
- **frontend/** : React SPA, multilingue, SEO
- **blockchain/** : smart contracts, scripts de déploiement
- **devops/** : Docker, Kubernetes, Terraform
- **docs/** : documentation technique et utilisateur
- **i18n/** : fichiers de traduction

---

## Bonnes pratiques de développement

- **Respecter la structure des dossiers**
- **Commenter et documenter chaque module/fonction critique**
- **Utiliser des variables d’environnement pour tous les secrets**
- **Ne jamais commiter de secrets ou credentials**
- **Écrire des tests unitaires pour chaque route/service critique**
- **Respecter les conventions de code (PEP8, ESLint, Prettier, etc.)**
- **Faire des PR atomiques et bien documentées**
- **Vérifier la sécurité (lint, audit, dépendances, headers, etc.)**

---

## Tests

- **Backend Flask** :  
  ```bash
  python -m unittest discover tests
  ```
- **Backend Node.js** :  
  ```bash
  npm test
  ```
- **Frontend** :  
  ```bash
  npm test
  ```

---

## Internationalisation

- Ajouter/modifier les fichiers de traduction dans `i18n/`
- Utiliser les utilitaires i18n dans le code (`utils/i18n.py`, `middleware/i18n.js`, etc.)
- Tester l’API et le frontend dans plusieurs langues

---

## Extensibilité

- Ajouter de nouveaux modules dans `app/services/`, `app/routes/`, `src/controllers/`, etc.
- Ajouter de nouveaux smart contracts dans `blockchain/contracts/`
- Ajouter des scripts DevOps dans `devops/`
- Ajouter des guides ou des exemples dans `docs/`

---

## CI/CD

- Utiliser GitHub Actions pour automatiser : lint, test, build, déploiement
- Exemple de workflow à placer dans `.github/workflows/ci.yml`

---

## Contribution

- Forker le projet, créer une branche, faire vos modifications, ouvrir une Pull Request
- Respecter la licence AGPL et les guidelines du projet
- Documenter toute nouvelle fonctionnalité ou modification majeure

---

## Support

Pour toute question ou bug, ouvrir une issue sur le dépôt GitHub ou contacter l’équipe Dihya Coding.

---

## Licence

Projet open-source sous licence AGPL.  
Voir le fichier `LICENSE` à la racine du projet.

---