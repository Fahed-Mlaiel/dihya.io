# Dihya Coding – Tests Notifications & Mailing

## Présentation

Ce dossier contient les tests automatisés pour le module de notifications et mailing de Dihya Coding. Ce module gère l’envoi de notifications (email, push, in-app) pour informer les utilisateurs des événements importants : génération de projet, paiement, sécurité, collaboration, etc. Les tests garantissent la fiabilité, la sécurité, la conformité RGPD et la robustesse de ces notifications.

---

## Objectifs des tests

- **Vérifier l’envoi correct des notifications (email, push, in-app)**
- **Assurer la gestion des erreurs d’envoi et des cas limites**
- **Tester la conformité RGPD (logs, audit, suppression/export)**
- **Garantir la non-exposition des secrets/API dans les logs**
- **Couvrir tous les cas d’usage métier (création projet, paiement, sécurité, etc.)**
- **Valider la personnalisation multilingue et la gestion des templates**

---

## Structure des tests

```
/notifications/tests/
├── test_email_send.py         # Tests envoi d’emails (SendGrid, Mailgun…)
├── test_push_notification.py  # Tests notifications push (web, mobile)
├── test_inapp_notification.py # Tests notifications in-app (UI/UX)
├── test_error_handling.py     # Tests gestion des erreurs d’envoi
├── test_rgpd_compliance.py    # Tests conformité RGPD (logs, suppression, export)
├── test_security.py           # Tests sécurité (masquage clés, accès restreint)
└── fixtures/                  # Données de test, mocks, configs simulées
```

---

## Bonnes pratiques

- **Tests unitaires et d’intégration** (pytest)
- **Mocks** pour simuler les services d’envoi externes
- **Validation stricte** des payloads et des templates
- **Logs horodatés** pour auditabilité
- **Vérification de la non-exposition des secrets**
- **Tests automatisés dans CI/CD (GitHub Actions)**
- **Documentation claire et cas d’usage reproductibles**

---

## Exemples de cas testés

- Envoi d’email de confirmation d’inscription
- Notification push lors de la génération d’un projet
- Notification in-app pour collaboration ou sécurité
- Erreur d’envoi (API down, quota dépassé) → gestion robuste
- Suppression/export des logs sur demande utilisateur (RGPD)
- Sécurité : aucune fuite de clé/API dans les logs ou réponses

---

## Lancer les tests

Depuis la racine du backend Flask :

```bash
pytest app/notifications/tests/
```

---

## Contribution

- Ajouter des cas de test pour chaque nouveau canal ou template de notification
- Respecter la structure et les conventions de nommage
- Documenter chaque test (docstring, typage)
- Vérifier la conformité RGPD et la sécurité à chaque PR

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---