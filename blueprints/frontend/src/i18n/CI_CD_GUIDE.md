# Guide CI/CD pour l’audit i18n

## Objectif
Automatiser la vérification de la conformité, complétude et qualité des fichiers de langue à chaque push/merge.

## Exemple de pipeline GitHub Actions
```yaml
name: Audit i18n
on:
  push:
    paths:
      - 'src/i18n/**'
  pull_request:
    paths:
      - 'src/i18n/**'
jobs:
  audit-i18n:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'
      - name: Install dependencies
        run: npm ci
      - name: Run i18n audit
        run: node src/i18n/audit_i18n.js
      - name: Générer badge et rapport
        run: node src/i18n/generate_i18n_docs.js
```

## Résultat attendu
- Badge de conformité mis à jour
- Rapport d’audit généré
- Blocage du merge en cas d’erreur ou de non-conformité

---

> Adapter le script d’audit selon les besoins métiers et la structure du projet.
