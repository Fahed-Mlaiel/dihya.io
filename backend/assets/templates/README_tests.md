# Dihya – Tests automatisés des templates backend

Ce dossier contient les scripts et la documentation pour l’audit automatisé des templates (emails, notifications, rapports) :

## Objectifs
- Vérifier la conformité RGPD, l’accessibilité (WCAG 2.1, ARIA), la présence de labels, le multilingue, et le contraste des couleurs.
- Générer un rapport d’audit pour chaque template (HTML, TXT, TEX).

## Critères vérifiés
- **Balises ARIA** : accessibilité des contenus HTML.
- **Mentions RGPD** : conformité légale.
- **Multilingue** : présence de sections ou balises pour FR, EN, AR, KAB.
- **Labels** : présence de labels pour les champs interactifs.
- **Contraste** : couleurs respectant les standards d’accessibilité.

## Utilisation
```bash
cd backend/assets/templates
chmod +x test_templates.sh
./test_templates.sh
cat test_templates_report.txt
```

## Interprétation
- `[OK]` : critère respecté.
- `[WARN]` : critère manquant ou à améliorer.

## Extension
- Ajoutez d’autres critères (ex : liens accessibles, structure sémantique, tests de rendu).
- Intégrez ce script dans la CI/CD pour garantir la conformité continue.
