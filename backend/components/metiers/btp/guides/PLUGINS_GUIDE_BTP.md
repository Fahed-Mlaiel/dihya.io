# Guide des Plugins BTP

Consignes pour le développement et l’intégration de plugins BTP.

## Structure d’un plugin BTP
- Fichier JS/Python exportant une classe ou fonction
- Méthodes : `execute`, `register`, `runHook`, `audit`, `export`, `anonymise`
- Sécurité : sandboxing, audit, logs, validation
- RGPD : anonymisation, export, consentement
- Accessibilité : audit, reporting
- Multilingue : messages, logs, erreurs

## Exemple (JS)
```js
class SEOPlugin {
  execute(chantier) {
    return { title: chantier.nom, description: chantier.description };
  }
}
```

## Hooks disponibles
- `btp_list`, `btp_create`, `btp_update`, `btp_delete`, `btp_export`, `btp_audit`

## Plugins recommandés
- SEO, RGPD, Accessibilité, Audit, IA fallback
