# integrations/tests/ — Tests d’intégration des webhooks & APIs externes (Dihya Coding)

Ce dossier contient les tests d’intégration pour la gestion sécurisée des webhooks et des APIs externes dans le backend Dihya Coding.

## Objectif

- Vérifier la bonne réception, validation et gestion des webhooks entrants.
- Tester l’envoi correct des webhooks sortants vers des services tiers.
- Garantir la robustesse, la sécurité et la conformité des intégrations externes.

## Bonnes pratiques

- Tester la validation des payloads (schéma, signature, etc.).
- Vérifier la gestion des erreurs, des cas limites et des réponses inattendues.
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les fixtures.
- Logger les résultats des tests pour audit et traçabilité.
- Prévoir des mocks pour éviter les appels réels aux services externes.

## Exemple de test

Voir `test_webhooks.py` pour un exemple de test sur la réception et l’envoi de webhooks.

## Sécurité

- Restreindre l’accès à ce dossier aux développeurs et à la CI.
- Ne jamais exposer les résultats de tests contenant des informations sensibles.

---

**Équipe Dihya Coding**