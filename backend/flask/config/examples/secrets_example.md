# secrets_example.md — Gestion sécurisée des secrets Dihya Coding

Ce fichier explique comment gérer les secrets et variables sensibles dans le backend Dihya Coding, en conformité avec les exigences de souveraineté, sécurité, RGPD et auditabilité.

---

## 🔒 Bonnes pratiques

- **Ne jamais stocker de secrets, credentials ou tokens dans le code source ou les dépôts publics.**
- Utiliser des fichiers `.env` ou des variables d’environnement pour toutes les clés/API/passwords.
- Ajouter `.env` dans `.gitignore` pour éviter tout commit accidentel.
- Restreindre l’accès aux fichiers de secrets (`chmod 600 .env`).
- Documenter chaque variable attendue pour faciliter le déploiement et l’audit.
- Utiliser des outils de gestion de secrets (Vault, Doppler, GitHub Secrets, AWS Secrets Manager…) en production.
- Toujours changer les secrets par défaut avant la mise en production.
- **Ne jamais exposer de secrets dans les logs, erreurs, ou interfaces utilisateur.**
- Pour la CI/CD, utiliser les variables d’environnement du pipeline (GitHub Actions, GitLab CI…).
- Prévoir un processus de rotation régulière des secrets.

---

## 📄 Exemple de fichier `.env` (à placer dans `backend/flask/.env`)

```env
# Flask
SECRET_KEY=change_me_please
JWT_SECRET_KEY=change_me_too

# Database
DATABASE_URL=sqlite:///dihya.db

# Mail
MAIL_SERVER=smtp.mailgun.org
MAIL_PORT=587
MAIL_USERNAME=postmaster@dihya.dev
MAIL_PASSWORD=supersecret
MAIL_DEFAULT_SENDER=no-reply@dihya.dev

# OAuth2 / Social Auth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret

# IA / API externes
OPENAI_API_KEY=your_openai_key
MISTRAL_API_KEY=your_mistral_key
LLAMA_API_KEY=your_llama_key

# DevOps / Monitoring
SENTRY_DSN=your_sentry_dsn
MONITORING_API_KEY=your_monitoring_key

# Mailing providers
SENDGRID_API_KEY=your_sendgrid_key
MAILGUN_API_KEY=your_mailgun_key

# Marketplace / Plugins
MARKETPLACE_API_KEY=your_marketplace_key

# RGPD / Compliance
AUDIT_LOG_PATH=./audit/logs
ENABLE_RGPD=True
```

---

## 🛡️ Sécurité & conformité

- Toujours supprimer les fichiers `.env` avant de partager ou publier le code.
- Ne jamais afficher les valeurs de secrets dans les logs, erreurs ou interfaces publiques.
- Pour la CI/CD, privilégier les variables d’environnement du pipeline sécurisé.
- Documenter chaque variable sensible dans la documentation technique.
- Prévoir des scripts d’audit pour vérifier l’absence de secrets dans le code versionné.
- Respecter la conformité RGPD : pas de données personnelles dans les exemples, anonymisation des logs de config.

---

## 📚 Ressources utiles

- [12 Factor App — Config](https://12factor.net/fr/config)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Dihya Coding — Guide d’installation backend](../examples/README.md)

---

**Dihya Coding** – Sécurité, conformité, souveraineté.