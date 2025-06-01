# Guide d'Onboarding Dihya Coding (FR)

## Introduction
Dihya Coding est une plateforme open source pour la gestion et le développement de projets IA, VR, AR, web et mobile, avec sécurité avancée, internationalisation dynamique, extensibilité, conformité RGPD, SEO, accessibilité et auditabilité.

## Démarrage rapide
1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/dihya-coding/dihya.git
   ```
2. **Préparer l'environnement :**
   - Python 3.10+, Node.js 18+, Docker requis.
   - Installer les dépendances :
     ```bash
     pip install -r requirements.txt
     npm install
     ```
3. **Lancer l'application :**
   ```bash
   make dev
   ```
4. **Connexion :**
   - Utilisez le compte invité ou créez un compte via l'interface web.

## Sécurité & conformité
- Chiffrement HTTPS, JWT, CORS, WAF, anti-DDOS.
- Conformité RGPD, logs d'audit, export des données.

## Internationalisation
- Prise en charge : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Contribution & support
- Voir `CONTRIBUTING_FR.md`.
- Ouvrir un ticket sur [GitHub Issues](https://github.com/dihya-coding/dihya/issues).

## Exemple : Créer un projet IA
```bash
curl -X POST /api/projects -H 'Authorization: Bearer <token>' -d '{"type": "ia"}'
```

## Liens clés
- [Guide sécurité](./securite_GUIDE_FR.md)
- [Roadmap](./ROADMAP_FR.md)
- [Documentation complète](./README_FR.md)

---
© 2025 Dihya Coding. Tous droits réservés.
