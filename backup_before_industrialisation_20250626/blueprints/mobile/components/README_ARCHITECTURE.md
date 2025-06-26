# Architecture des composants

- Respect du pattern Atomic Design (atoms, molecules, organisms, templates)
- Chaque composant est documenté, testé, versionné
- Les composants sont réutilisables, accessibles, internationalisables
- Tous les exports sont centralisés dans `index.js` à chaque niveau

## Schéma d’architecture (ASCII)

[Atoms] → [Molecules] → [Organisms] → [Templates] → [Pages]

## Exemple d’architecture
```
components/
  atoms/
    Button.jsx
    Input.jsx
    ...
  molecules/
    CardUser.jsx
    FormField.jsx
    ...
  organisms/
    Navbar.jsx
    Sidebar.jsx
    ...
  templates/
    DashboardTemplate.jsx
    AuthTemplate.jsx
    ...
```

## Convention Lead Dev
- Atomicité, accessibilité, typage, multilingue, branding
- Props typées, logique UI isolée, style modulaire, documentation intégrée
- Export via index.js à chaque niveau
