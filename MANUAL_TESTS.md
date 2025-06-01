# 🧑‍💻 Dihya – Plan de Tests Manuels Multistack & Multilingue

---

## Table des matières

- [Introduction](#introduction)
- [Principes des tests manuels](#principes-des-tests-manuels)
- [Checklist globale](#checklist-globale)
- [Scénarios Frontend (React)](#scénarios-frontend-react)
- [Scénarios Backend (Flask/Node/Django)](#scénarios-backend-flasknodedjango)
- [Scénarios Mobile (Flutter)](#scénarios-mobile-flutter)
- [Tests d’accessibilité](#tests-daccessibilité)
- [Tests multilingues](#tests-multilingues)
- [Tests de sécurité](#tests-de-sécurité)
- [Traçabilité & conformité](#traçabilité--conformité)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document décrit le plan de tests manuels pour le projet **Dihya**. Il complète les tests automatisés (unit, integration, e2e) et garantit la robustesse, la sécurité, l’accessibilité, la conformité RGPD, la souveraineté numérique, et la compatibilité multi-stack (React, Flask, Node, Django, Flutter…).

---

## Principes des tests manuels

- **Complémentarité** : couvrir les cas non testés automatiquement.
- **Traçabilité** : chaque test est tracé, daté, et signé.
- **Multilingue** : chaque scénario est testé en fr, en, ar, tzm.
- **Accessibilité** : tests avec lecteurs d’écran, navigation clavier, contrastes.
- **Sécurité** : vérification MFA, gestion des erreurs, absence de fuite de données.
- **Conformité** : RGPD, accessibilité, souveraineté, open source.

---

## Checklist globale

- [ ] Application accessible et fonctionnelle sur tous les navigateurs/supports.
- [ ] Navigation clavier et lecteurs d’écran opérationnels.
- [ ] MFA et gestion des sessions testés.
- [ ] Consentement RGPD affiché et journalisé.
- [ ] Fallback IA open source opérationnel.
- [ ] Logs et erreurs non exposés à l’utilisateur.
- [ ] Fonctionnalités principales testées dans chaque langue.
- [ ] Aucune donnée personnelle en clair dans les logs ou l’UI.
- [ ] Rollback automatique testé en cas d’échec déploiement.
- [ ] Documentation multilingue accessible.

---

## Scénarios Frontend (React)

| ID      | Scénario                                      | Langues | Résultat attendu                | Statut | Date       | Testeur      |
|---------|-----------------------------------------------|---------|---------------------------------|--------|------------|--------------|
| FE-001  | Connexion avec MFA                            | fr/en/ar/tzm | Accès sécurisé, MFA requis      |        |            |              |
| FE-002  | Navigation clavier sur tous les menus         | fr/en/ar/tzm | Navigation fluide, focus visible|        |            |              |
| FE-003  | Affichage du consentement RGPD                | fr/en/ar/tzm | Consentement affiché et journalisé |    |            |              |
| FE-004  | Changement de langue dynamique                | fr/en/ar/tzm | UI traduite instantanément      |        |            |              |
| FE-005  | Message d’erreur non technique à l’utilisateur| fr/en/ar/tzm | Message clair, pas de stacktrace|        |            |              |

---

## Scénarios Backend (Flask/Node/Django)

| ID      | Scénario                                      | Résultat attendu                | Statut | Date       | Testeur      |
|---------|-----------------------------------------------|---------------------------------|--------|------------|--------------|
| BE-001  | API refuse accès sans authentification        | 401 Unauthorized                |        |            |              |
| BE-002  | Logs anonymisés, pas de données perso         | Logs sans données sensibles     |        |            |              |
| BE-003  | Rollback automatique sur erreur critique      | Service restauré, logs présents |        |            |              |
| BE-004  | Fallback IA open source activé                | Réponse IA locale si cloud KO   |        |            |              |
| BE-005  | Export logs conforme RGPD                     | Export anonymisé, traçable      |        |            |              |

---

## Scénarios Mobile (Flutter)

| ID      | Scénario                                      | Résultat attendu                | Statut | Date       | Testeur      |
|---------|-----------------------------------------------|---------------------------------|--------|------------|--------------|
| MO-001  | Installation sur Android/iOS                  | Lancement sans crash            |        |            |              |
| MO-002  | Changement de langue dans l’app               | UI traduite instantanément      |        |            |              |
| MO-003  | Accessibilité (VoiceOver/TalkBack)            | Lecture correcte, navigation OK |        |            |              |
| MO-004  | MFA sur mobile                                | Authentification MFA OK         |        |            |              |
| MO-005  | Notification RGPD                             | Consentement affiché            |        |            |              |

---

## Tests d’accessibilité

- Navigation clavier sur toutes les pages.
- Tests avec lecteurs d’écran (NVDA, VoiceOver, Orca).
- Vérification des contrastes (WCAG AA/AAA).
- Focus visible et logique.
- Absence de piège clavier.

---

## Tests multilingues

- Tester chaque fonctionnalité en français, anglais, arabe, amazigh.
- Vérifier la cohérence des traductions et l’absence de texte non traduit.
- Tester les formulaires, erreurs, notifications dans chaque langue.

---

## Tests de sécurité

- MFA obligatoire sur tous les accès sensibles.
- Tentative d’accès non autorisé : refusé, loggé, sans fuite d’info.
- Injection XSS/SQL : aucune faille détectée.
- Logs et erreurs non exposés à l’utilisateur.
- Fallback IA open source testé (Ollama, LocalAI…).

---

## Traçabilité & conformité

- Chaque test manuel est tracé dans ce document (date, testeur, statut).
- Les écarts sont déclarés via GitHub Issues ou email (voir contacts).
- Les preuves (captures, logs, vidéos) sont archivées dans `/tests/manual/proofs/`.

---

## Templates & exemples

### Template de test manuel

```
- ID : [ex. FE-001]
- Fonctionnalité : [ex. Connexion MFA]
- Stack : [ex. Frontend/React]
- Langue : [fr/en/ar/tzm]
- Résultat attendu : [ex. MFA requis, accès OK]
- Résultat obtenu :
- Statut : OK / KO
- Date :
- Testeur :
- Preuve : [capture/log/vidéo]
- Commentaire :
```

### Exemple rempli

```
- ID : FE-001
- Fonctionnalité : Connexion MFA
- Stack : Frontend/React
- Langue : fr
- Résultat attendu : MFA requis, accès OK
- Résultat obtenu : MFA affiché, accès OK
- Statut : OK
- Date : 2025-05-20
- Testeur : @qa-lead
- Preuve : /tests/manual/proofs/FE-001_fr.png
- Commentaire : RAS
```

---

## Multilingue

- **Français** : Ce plan est disponible en français.
- **English** : This plan is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-qa
- **Email** : qa@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce plan de tests manuels est validé pour la production. Toute modification doit être soumise via PR et validée par le QA Lead et le RSSI.**

# Guide des tests manuels Dihya

- Checklist de tests manuels (UI, accessibilité, sécurité, performance)
- Procédures de test, scénarios, validation multilingue
- Reporting, gestion des bugs, feedback utilisateurs
- Intégration avec les tests automatisés

Voir [E2E_TESTS_GUIDE.md](E2E_TESTS_GUIDE.md), [TESTS_README.md](docs/TESTS_README.md)
