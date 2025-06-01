# 🛡️ Guide Utilisateur Dihya Coding

Bienvenue sur Dihya Coding, la première plateforme No-Code/Low-Code capable de générer automatiquement des projets numériques complets (frontend + backend) à partir d’un cahier des charges écrit ou dicté, avec un design moderne, une sécurité avancée, une conformité RGPD et une extensibilité maximale.

---

## 🚀 Qu’est-ce que Dihya Coding ?

Dihya Coding est une plateforme intelligente qui permet de :
- Générer des applications web (React/Vue/Svelte)
- Générer des applications mobiles (React Native/Flutter)
- Générer des APIs (Flask, Node.js, Django)
- Générer des scripts IA, DevOps, Blockchain
- Personnaliser le design (Tailwind/Material UI) avec des thèmes amazighs ou modernes
- Gérer le multilingue et les dialectes

---

## 🏁 Démarrage rapide

1. **Inscription et connexion**
   - Cliquez sur le bouton d’inscription/connexion en haut
   - Authentification sécurisée via OAuth/JWT
   - Vérification de l’email obligatoire

2. **Créer un nouveau projet**
   - Saisissez la description du projet (texte ou voix)
   - Choisissez le type de projet (Web, Mobile, API, etc.)
   - Personnalisez les options (design, langue, plugins...)

3. **Prévisualisation et génération**
   - Prévisualisez en direct (GitHub Pages/Replit)
   - Téléchargez le code ou partagez un lien de démo

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

## 🛡️ Sécurité & confidentialité

- **JWT/OAuth** pour toutes les opérations sensibles
- **Rate Limiting** pour éviter les abus
- **CORS strict** configuré
- **Chiffrement des données** au repos et en transit
- **Logs d’audit** pour toutes les actions critiques
- **Conformité RGPD** (droit à l’oubli, export, consentement)
- **Audit automatique des vulnérabilités et configurations**

---

## 🌍 Multilingue & dialectes

- Support automatique du français, amazigh, arabe, anglais et dialectes
- Traduction dynamique par IA
- Personnalisation des traductions possible

---

## 🎨 Design & identité

- Interface moderne et responsive
- Thèmes inspirés de la culture amazighe ou high-tech
- Couleurs et logo personnalisables

---

## ⚙️ Extensibilité & plugins

- Support des plugins Analytics, Stripe, CMS, etc.
- Système de templates intelligent par domaine (e-commerce, éducation, social...)
- Intégration facile de plugins personnalisés

---

## 📜 Conformité & transparence

- **Projet open-source (AGPL)**
- Documentation complète de chaque génération (logs horodatés)
- Politique de confidentialité et sécurité claire
- Vérification de l’origine du code généré

---

## 📝 Bonnes pratiques

- Validez toutes les entrées utilisateur
- Utilisez des mots de passe forts
- Consultez régulièrement les logs de génération
- Mettez à jour vos plugins
- Surveillez la performance et la sécurité depuis le dashboard

---

## ❓ Support & aide

- [Guide utilisateur français](./guide_fr.md)
- [Guide utilisateur amazigh](./guide_ber.md)
- [Guide utilisateur arabe](./guide_ar.md)
- [Guide utilisateur anglais](./guide_en.md)
- Contact : contact@dihya.coding

---

> **Slogan :** De l’idée au code, en toute souveraineté et transparence.
