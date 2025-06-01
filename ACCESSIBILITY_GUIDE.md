# Guide d’accessibilité Dihya

Ce guide détaille toutes les bonnes pratiques et exigences d’accessibilité numérique appliquées à la plateforme Dihya : conformité WCAG 2.2, navigation clavier, ARIA, contrastes, multilingue, tests automatisés, audit Lighthouse, etc. Pour chaque composant, vérifiez :
- Navigation clavier complète
- Contrastes respectés (AA/AAA)
- Textes alternatifs pour les images
- Support des lecteurs d’écran (NVDA, VoiceOver…)
- Multilingue et direction du texte (RTL/LTR)
- Tests automatisés d’accessibilité (axe, pa11y, Lighthouse)

Pour contribuer : voir [CONTRIBUTING.md](CONTRIBUTING.md) et [ACCESSIBILITY_GUIDE_ADVANCED.md](ACCESSIBILITY_GUIDE_ADVANCED.md).

---

## 🌍 Multilingue & Inclusion | Multilingual & Inclusion | التعدد اللغوي والشمول | ⵜⴰⵎⴰⵣⵉⵖⵜ

- Documentation, UI, messages d’erreur et guides disponibles en **français, anglais, arabe, amazigh**.
- Traductions vérifiées par des natifs, fallback IA open source pour la génération de contenu accessible.
- Navigation et feedback adaptés à tous les profils : débutant, expert, malvoyant, daltonien, utilisateur clavier, lecteur d’écran.

---

## 🏗️ Principes de base

- **Contraste élevé** (AA/AAA), thèmes personnalisables, testés avec simulateurs de déficiences visuelles.
- **Navigation clavier** : tous les composants sont accessibles sans souris (tabindex, focus visible, skip links).
- **ARIA & rôles sémantiques** : balises et attributs ARIA systématiques, rôles explicites pour chaque composant.
- **Responsive** : UI testée sur mobile, desktop, lecteurs d’écran, zoom x200%.
- **Animations** : désactivables, non bloquantes, respect du prefers-reduced-motion.
- **Formulaires** : labels explicites, erreurs vocalisées, aides contextuelles multilingues.

---

## 🧪 Tests & audits

- **CI/CD** : chaque build lance des tests d’accessibilité (axe, pa11y, Lighthouse, jest-axe, cypress-axe).
- **Couverture** : 100% des pages critiques testées (unit, integration, e2e, audit manuel).
- **Rapports** : export HTML, JSON, badge d’accessibilité dans le README.
- **Audit manuel** : checklist WCAG, RGAA, Section 508, tests utilisateurs réels.

---

# ACCESSIBILITY_GUIDE.md

# Guide d’Accessibilité – Dihya Coding

## Objectifs
- Accessibilité (WCAG 2.1, ARIA, navigation clavier, multilingue)
- RGPD, sécurité, SEO backend, plugins, auditabilité, CI/CD-ready

## Procédures
1. **Design** : contrastes, navigation clavier, ARIA, multilingue
2. **Développement** : tests automatisés (axe-core, lighthouse), plugins
3. **Audit** : reporting, logs, conformité RGPD, accessibilité, SEO

## Outils recommandés
- axe-core, lighthouse, custom scripts, CI/CD pipelines

## Documentation intégrée
- Voir aussi: ACCESSIBILITY_GUIDE_ADVANCED.md, AUDIT_LOGGING_GUIDE.md, LEGAL_COMPLIANCE_GUIDE.md

---

Pour toute question, contacter l’équipe accessibilité.

---

## 🔄 Exemples de bonnes pratiques

### React (JSX)

```jsx
<button aria-label="Ajouter au panier" lang="fr" onClick={handleAdd} tabIndex={0}>
  <span role="img" aria-label="Panier">🛒</span> Ajouter
</button>
```

### HTML

```html
<label for="email" lang="en">Email address</label>
<input id="email" name="email" type="email" required aria-required="true" aria-describedby="emailHelp" />
<small id="emailHelp" lang="ar">سيتم استخدام بريدك الإلكتروني فقط للمصادقة.</small>
```

### Flutter

```dart
Semantics(
  label: 'ⴰⵙⵉⵏⴰⵡ ⴷ ⴰⵎⴰⵣⵉⵖ',
  child: ElevatedButton(
    onPressed: () => login(),
    child: Text('Login'),
  ),
)
```

---

## 📋 Checklist accessibilité Dihya

- [x] Contraste AA/AAA vérifié
- [x] Navigation clavier complète
- [x] Focus visible et logique
- [x] ARIA roles et labels explicites
- [x] Multilingue sur tous les textes et aides
- [x] Tests automatisés et manuels à chaque release
- [x] Feedback utilisateur vocalisé et visuel
- [x] Documentation et guides accessibles

---

## 🚨 Procédure de signalement accessibilité

1. **Décrivez le problème** (page, composant, langue, device, navigateur)
2. **Contactez** : [accessibilite@dihya.coding](mailto:accessibilite@dihya.coding)
3. **Réponse sous 72h**, correction prioritaire, suivi transparent

---

## 📚 Ressources associées

- [ACCESSIBILITY_GUIDE_ADVANCED.md](./ACCESSIBILITY_GUIDE_ADVANCED.md)
- [README.md](./README.md)
- [securite.md](./Dihya/securite.md)
- [docs/accessibility/](./docs/accessibility/)
- [WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)
- [Section 508](https://www.section508.gov/)

---

> **Dihya Coding : accessibilité, inclusion, souveraineté, innovation pour tous.**
