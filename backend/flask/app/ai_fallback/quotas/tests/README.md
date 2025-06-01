# Dihya Coding – Tests AI Fallback & Quotas

## Présentation

Ce dossier contient les tests automatisés pour le module de gestion des quotas et fallback IA de Dihya Coding. Ce module garantit la continuité du service IA (GPT, Mixtral, LLaMA, Mistral…) en cas de dépassement de quotas, d’indisponibilité API ou de censure, conformément à la stratégie de souveraineté numérique du projet.

---

## Objectifs des tests

- **Vérifier la détection automatique du dépassement de quotas API**
- **Assurer le basculement automatique vers un modèle IA open source local**
- **Garantir la continuité du service IA pour l’utilisateur final**
- **Tester la robustesse face aux erreurs réseau, limitations, ou blocages**
- **Valider la conformité RGPD (logs, audit, suppression/export)**
- **Assurer la sécurité et la non-exposition des clés/API sensibles**
- **Couvrir tous les cas d’usage métier (génération, correction, suggestion, chat IA, etc.)**

---

## Structure des tests

```
/ai_fallback/quotas/tests/
├── test_quota_detection.py      # Tests détection de quotas dépassés (OpenAI, autres)
├── test_fallback_switch.py      # Tests bascule automatique vers fallback local (Mixtral, LLaMA…)
├── test_error_handling.py       # Tests gestion des erreurs API/réseau
├── test_rgpd_compliance.py      # Tests conformité RGPD (logs, suppression, export)
├── test_security.py             # Tests sécurité (masquage clés, accès restreint)
└── fixtures/                    # Données de test, mocks, configs simulées
```

---

## Bonnes pratiques

- **Tests unitaires et d’intégration** (pytest)
- **Mocks** pour simuler les réponses API et quotas dépassés
- **Logs horodatés** pour auditabilité
- **Vérification de la non-exposition des secrets**
- **Tests automatisés dans CI/CD (GitHub Actions)**
- **Documentation claire et cas d’usage reproductibles**

---

## Exemples de cas testés

- Dépassement de quota OpenAI → bascule automatique Mixtral local
- Indisponibilité réseau → fallback LLaMA/Mistral
- Logs d’audit générés et exportables
- Suppression des logs sur demande utilisateur (RGPD)
- Génération IA toujours disponible pour l’utilisateur final
- Sécurité : aucune fuite de clé/API dans les logs ou réponses

---

## Lancer les tests

Depuis la racine du backend Flask :

```bash
pytest app/ai_fallback/quotas/tests/
```

---

## Contribution

- Ajouter des cas de test pour chaque nouveau fallback ou modèle IA intégré
- Respecter la structure et les conventions de nommage
- Documenter chaque test (docstring, typage)
- Vérifier la conformité RGPD et la sécurité à chaque PR

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---