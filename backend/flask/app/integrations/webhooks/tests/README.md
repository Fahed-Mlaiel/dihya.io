# Dihya Coding – Tests Intégrations Webhooks

## Présentation

Ce dossier contient les tests automatisés pour le module d’intégration et de gestion des webhooks de Dihya Coding. Les webhooks permettent à la plateforme de communiquer en temps réel avec des services externes (GitHub, Stripe, SendGrid, etc.), d’automatiser des workflows, de recevoir des notifications ou de déclencher des actions métiers. Les tests garantissent la fiabilité, la sécurité, la conformité RGPD et la robustesse de ces intégrations.

---

## Objectifs des tests

- **Vérifier la réception et la validation sécurisée des webhooks entrants**
- **Assurer la gestion correcte des événements métiers (push, paiement, notification, etc.)**
- **Tester la résilience face aux erreurs réseau, duplications, ou payloads malformés**
- **Garantir la conformité RGPD (logs, audit, suppression/export)**
- **Assurer la non-exposition des secrets et la sécurité des endpoints**
- **Couvrir tous les cas d’usage métier (CI/CD, paiement, mailing, analytics, etc.)**

---

## Structure des tests

```
/integrations/webhooks/tests/
├── test_github_webhook.py      # Tests intégration GitHub (push, PR, CI/CD)
├── test_stripe_webhook.py      # Tests intégration Stripe (paiement, abonnement)
├── test_sendgrid_webhook.py    # Tests intégration SendGrid (mailing, bounce, event)
├── test_custom_webhook.py      # Tests webhooks métiers personnalisés
├── test_security.py            # Tests sécurité (signature, validation, accès)
├── test_rgpd_compliance.py     # Tests conformité RGPD (logs, suppression, export)
└── fixtures/                   # Données de test, mocks, configs simulées
```

---

## Bonnes pratiques

- **Tests unitaires et d’intégration** (pytest)
- **Mocks** pour simuler les payloads et signatures externes
- **Validation stricte** des signatures et des schémas de payload
- **Logs horodatés** pour auditabilité
- **Vérification de la non-exposition des secrets**
- **Tests automatisés dans CI/CD (GitHub Actions)**
- **Documentation claire et cas d’usage reproductibles**

---

## Exemples de cas testés

- Réception d’un push GitHub → déclenchement CI/CD interne
- Paiement Stripe réussi → activation d’abonnement utilisateur
- Notification SendGrid → mise à jour du statut d’email
- Webhook mal signé ou payload invalide → rejet sécurisé
- Suppression/export des logs sur demande utilisateur (RGPD)
- Sécurité : aucune fuite de clé/API dans les logs ou réponses

---

## Lancer les tests

Depuis la racine du backend Flask :

```bash
pytest app/integrations/webhooks/tests/
```

---

## Contribution

- Ajouter des cas de test pour chaque nouveau service ou webhook intégré
- Respecter la structure et les conventions de nommage
- Documenter chaque test (docstring, typage)
- Vérifier la conformité RGPD et la sécurité à chaque PR

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---