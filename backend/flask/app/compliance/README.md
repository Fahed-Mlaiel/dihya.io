# Scripts d'audit conformité (accessibilité, RGPD...)

Ce dossier regroupe les scripts et modules dédiés à la conformité réglementaire et à l’accessibilité du backend Dihya Coding.

## Objectif

Garantir que la plateforme respecte les exigences légales (RGPD, souveraineté numérique, etc.) et les standards d’accessibilité numérique.

## Bonnes pratiques Dihya Coding

- **Auditabilité** : fournir des scripts pour vérifier la conformité des traitements de données, la gestion des consentements, la traçabilité des accès, etc.
- **Accessibilité** : intégrer des outils d’audit pour s’assurer que les interfaces et API sont utilisables par tous (normes WCAG, ARIA, etc.).
- **Sécurité** : ne jamais exposer de données personnelles dans les rapports d’audit.
- **Documentation** : chaque script doit être documenté (usage, portée, limitations).
- **Automatisation** : prévoir l’exécution automatique de certains audits (CI/CD, cron, etc.).

## Exemples de scripts à inclure

- `audit_rgpd.py` : vérification du respect des droits utilisateurs (accès, suppression, portabilité…)
- `audit_accessibilite.py` : contrôle de la conformité des endpoints et interfaces API
- `reporting.py` : génération de rapports de conformité anonymisés
- `README.md` : documentation sur l’utilisation et l’extension des scripts

## Utilisation

Lancer un audit RGPD :

```bash
python compliance/audit_rgpd.py
```

Automatiser dans un pipeline CI/CD :

```yaml
- name: Audit RGPD
  run: python compliance/audit_rgpd.py
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*