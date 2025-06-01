# 🛡️ Dihya Coding – Documentation Utilisateur

Bienvenue dans la documentation utilisateur de Dihya Coding, la première plateforme No-Code/Low-Code qui génère automatiquement des projets numériques complets (frontend + backend) à partir d’un cahier des charges écrit ou dicté.  
Cette documentation garantit : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et bonnes pratiques.

---

## 🚀 Présentation

Dihya Coding permet de :
- Générer des applications web, mobiles, APIs, scripts IA, DevOps, Blockchain
- Personnaliser le design (UI/UX responsive, thèmes amazighs ou modernes)
- Gérer le multilingue et les dialectes
- Intégrer des plugins (Analytics, Stripe, CMS, etc.)
- Déployer automatiquement (GitHub Pages, Replit, Render...)

---

## 🗺️ Fonctions principales & routes

| Fonction                | Route                    | Description                              | Sécurité/Validation   |
|-------------------------|--------------------------|------------------------------------------|-----------------------|
| Inscription utilisateur | `/api/auth/register`     | Création de compte utilisateur           | Vérif. email, Captcha |
| Connexion               | `/api/auth/login`        | Connexion sécurisée                      | JWT, Rate Limiting    |
| Génération de projet    | `/api/generate`          | Générer un projet à partir du cahier     | Vérif. rôle, Anti-DDoS|
| Prévisualisation        | `/api/preview`           | Prévisualisation du projet               | Vérif. utilisateur    |
| Gestion des plugins     | `/api/plugins`           | Ajouter/supprimer des plugins            | Vérif. rôle           |
| Traduction automatique  | `/api/i18n/translate`    | Traduction automatique du projet         | Vérif. utilisateur    |
| Envoi d’email           | `/api/mail/send`         | Envoi d’email via API                    | Rôle, Rate Limiting   |
| Téléchargement backup   | `/api/backup/download`   | Télécharger une sauvegarde du projet     | Vérif. utilisateur    |
| Logs de génération      | `/api/logs/generation`   | Historique des générations               | Admin uniquement      |

---

## 🛡️ Sécurité & conformité

- Authentification OAuth/JWT
- Rate Limiting & Anti-DDoS
- CORS strict
- Chiffrement des données (repos & transit)
- Logs d’audit pour toutes les actions critiques
- Conformité RGPD (droit à l’oubli, export, consentement)
- Audit automatique des vulnérabilités

---

## 🌍 Multilingue & accessibilité

- Documentation disponible en français, anglais, arabe, amazigh
- Traduction dynamique IA
- Accessibilité renforcée (UI responsive, navigation clavier)

---

## 🎨 Design & extensibilité

- Interface moderne, responsive, SEO friendly
- Thèmes personnalisables (couleurs, logo, branding amazigh)
- Système de plugins et templates métiers

---

## 📜 Transparence & bonnes pratiques

- Projet open-source (AGPL)
- Documentation complète et logs horodatés
- Vérification de l’origine du code généré
- Validation stricte des entrées utilisateur
- Mises à jour régulières et auditabilité

---

## 📚 Guides disponibles

- [Guide utilisateur français](./guide_fr.md)
- [Guide utilisateur anglais](./guide_en.md)
- [Guide utilisateur arabe](./guide_ar.md)
- [Guide utilisateur amazigh](./guide_ber.md)

---

## ❓ Support

Pour toute question ou aide, contactez : contact@dihya.coding

---

> **Slogan :** De l’idée au code, en toute souveraineté et transparence.
